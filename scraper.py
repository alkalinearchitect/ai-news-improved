#!/usr/bin/env python3
"""
AI News Scraper & Site Generator
Scrapes latest AI articles from artificialintelligence-news.com
and generates a clean, fast static site with no cookie wall or ad clutter.
"""
import requests
import re
import json
import os
import html
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

BASE_URL = "https://www.artificialintelligence-news.com"
NEWS_URL = f"{BASE_URL}/news/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

class ArticleExtractor(HTMLParser):
    """Extract article content from HTML, stripping ads, nav, cookie banners."""
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.in_article = False
        self.in_entry_content = False
        self.in_title = False
        self.in_author = False
        self.in_date = False
        self.skip_depth = 0
        self.title = ""
        self.author = ""
        self.date_str = ""
        self.content_parts = []
        self.image_url = ""
        self.tags = []
        self.categories = []
        self.in_skip_zone = False

        # Elements to skip (ads, banners, cookie consent, footers)
        self.SKIP_TAGS = {
            "aside", "nav", "footer", "header",
            "script", "style", "iframe", "noscript",
            "form", "button", "input",
            "div#cookie-container", "div#accept-cookies",
            "div.cookie-consent", "div.gdpr",
            "div.advertisement", "div.ad-wrapper",
            "div.sponsor", "div.partner-banner",
        }
        self.skip_classes = [
            "cookie", "consent", "gdpr", "ad-", "advert",
            "sponsor", "partner-banner", "popup", "modal",
            "newsletter", "subscribe-form", "social-share",
            "related-posts", "tags", "categories", "footer",
            "header", "navbar", "menu", "sidebar"
        ]
        self.SKIP_IDS = {"cookie-container", "accept-cookies", "subscribe", "footer", "header"}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        class_list = attrs_dict.get("class", "")
        id_val = attrs_dict.get("id", "")

        # Check if we should skip this element
        if self._should_skip(tag, class_list, id_val):
            self.skip_depth += 1
            self.in_skip_zone = True
            return

        # Look for the main article content
        if tag == "article":
            self.in_article = True
            self.in_entry_content = True
        elif tag == "h1" and self.in_article:
            self.in_title = True
        elif tag == "p" and self.in_entry_content:
            self.content_parts.append("\n\n")
        elif tag in ("a",) and self.in_article:
            href = attrs_dict.get("href", "")
            # Check for category tags
            if href and "/categories/" in href and self.in_article:
                pass  # handled in text

        # Collect image
        if tag == "img" and self.in_article and not self.image_url:
            src = attrs_dict.get("src", "") or attrs_dict.get("data-src", "")
            if src:
                self.image_url = src

    def _should_skip(self, tag, class_str, id_str):
        if tag in self.SKIP_TAGS:
            return True
        if tag == "div":
            if id_str in self.SKIP_IDS:
                return True
            for cls in class_str.split():
                if cls in self.skip_classes or cls.startswith("cookie") or cls.startswith("ad-"):
                    return True
        return False

    def handle_endtag(self, tag):
        if self.skip_depth > 0:
            if tag in ("aside", "nav", "footer", "header", "div"):
                self.skip_depth -= 1
                if self.skip_depth == 0:
                    self.in_skip_zone = False
            return
        if tag == "article":
            self.in_article = False
            self.in_entry_content = False
        elif tag == "h1" and self.in_title:
            self.in_title = False

    def handle_data(self, data):
        if self.in_skip_zone:
            return
        if self.in_title:
            self.title += data
        elif self.in_entry_content:
            self.content_parts.append(data)


def get_article_links():
    """Get latest article links from the news page."""
    try:
        resp = requests.get(NEWS_URL, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching news page: {e}")
        return []

    # Find all article links
    link_pattern = r'href="(https?://www\.artificialintelligence-news\.com/news/[^"]+)"'
    links = re.findall(link_pattern, resp.text)
    
    # Deduplicate and return unique links, preserving order
    seen = set()
    unique_links = []
    for link in links:
        if link not in seen:
            seen.add(link)
            unique_links.append(link)
    
    return unique_links[:15]


def extract_article(url):
    """Extract article data from a single URL."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching article {url}: {e}")
        return None

    html_text = resp.text

    # Extract title from JSON-LD or og:title
    title = ""
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_text, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
    
    if not title:
        og_title = re.search(r'og:title"[^>]*content="([^"]+)"', html_text)
        if og_title:
            title = html.unescape(og_title.group(1)).strip()

    # Extract date
    date = ""
    date_match = re.search(r'<time[^>]*datetime="([^"]+)"', html_text)
    if date_match:
        date = date_match.group(1)
    else:
        # Try to find date in text
        date_match = re.search(r'/(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})/i', html_text)
        if date_match:
            date = date_match.group(0)

    # Extract author
    author = ""
    author_match = re.search(r'By\s+<a[^>]*href="[^"]*author[^"]*"[^>]*>(.*?)</a>', html_text, re.DOTALL)
    if author_match:
        author = re.sub(r'<[^>]+>', '', author_match.group(1)).strip()
    
    if not author:
        author_match = re.search(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"([^"]+)"', html_text)
        if author_match:
            author = author_match.group(1)

    # Extract featured image
    image_url = ""
    img_match = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html_text)
    if img_match:
        image_url = img_match.group(1)

    # Extract description
    description = ""
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html_text)
    if desc_match:
        description = html.unescape(desc_match.group(1)).strip()

    if not description:
        # Try to extract first paragraph with substantial content
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html_text, re.DOTALL)
        for para in paragraphs:
            clean = re.sub(r'<[^>]+>', '', para).strip()
            if len(clean) > 100 and not any(skip in clean.lower() for skip in ["skip to", "subscribe", "cookie", "manage", "by submitting"]):
                description = clean
                break

    # Extract full body content
    body = extract_body_content(html_text)

    # Extract tags
    tags = []
    tag_matches = re.findall(r'href="[^"]*tag/([^"]+)"', html_text)
    tags = [t.replace("-", " ").title() for t in tag_matches[:15]]

    # Extract categories  
    categories = []
    cat_matches = re.findall(r'href="[^"]*categories/([^"]+)"', html_text)
    categories = [c.replace("-", " ").title() for c in cat_matches[:10]]

    return {
        "url": url,
        "title": title or "Untitled",
        "author": html.unescape(author) if author else "Staff Writer",
        "date": date or datetime.now().strftime("%B %d, %Y"),
        "description": html.unescape(description) if description else "",
        "body": html.unescape(body) if body else "",
        "image": image_url,
        "tags": list(set(tags)),
        "categories": list(set(categories)),
    }


def extract_body_content(html_text):
    """Extract main article body content, stripping ads/nav/etc."""
    # Find the main content area
    # Look for the entry-content or article-content div
    content = ""
    
    # Try to find main article body
    body_match = re.search(
        r'<div[^>]*class="[^"]*entry-content[^"]*"[^>]*>(.*?)</div>\s*<!--\s*\.entry-content',
        html_text, re.DOTALL
    )
    if not body_match:
        body_match = re.search(
            r'<div[^>]*class="[^"]*td-post-content[^"]*"[^>]*>(.*?)</div>\s*<!--\s*\.td-post-content',
            html_text, re.DOTALL
        )
    if not body_match:
        body_match = re.search(
            r'<div[^>]*class="[^"]*article-body[^"]*"[^>]*>(.*?)</div>\s*</div>',
            html_text, re.DOTALL
        )
    
    if body_match:
        content = body_match.group(1)
    else:
        # Fallback: get all paragraphs and filter
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html_text, re.DOTALL)
        meaningful = []
        for para in paragraphs:
            clean = re.sub(r'<[^>]+>', '', para).strip()
            if len(clean) > 50 and not any(skip in clean.lower() for skip in [
                "skip to", "subscribe", "cookie", "manage consent", "by submitting",
                "view all", "click here", "learn more about physical ai",
                "see also:", "share this story", "advertisement",
                "powered by", "terms", "privacy"
            ]):
                meaningful.append(clean)
        content = "\n\n".join(meaningful)

    # Clean up the content
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<iframe[^>]*>.*?</iframe>', '', content, flags=re.DOTALL)
    
    # Remove cookie/ad divs
    content = re.sub(r'<div[^>]*class="[^"]*(?:cookie|consent|gdpr|advert|sponsor|popup|modal|newsletter)[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    
    # Convert some HTML to readable format
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n\n## \1\n\n', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n\n### \1\n\n', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', content, flags=re.DOTALL)
    content = re.sub(r'<br\s*/?>', '\n\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'\n\n• \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\n\1\n', content, flags=re.DOTALL)
    content = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\n\1\n', content, flags=re.DOTALL)
    
    content = re.sub(r'<[^>]+>', '', content)
    content = html.unescape(content)
    
    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'[ \t]{2,}', ' ', content)
    content = content.strip()
    
    return content


def scrape_all():
    """Scrape all latest articles and return structured data."""
    links = get_article_links()
    articles = []
    
    for i, link in enumerate(links):
        print(f"  Scraping {i+1}/{len(links)}: {link}")
        article = extract_article(link)
        if article:
            articles.append(article)
        if i >= 10:  # Limit to top 10 for now
            break
    
    return articles


def generate_site(articles, output_dir):
    """Generate full static site from article data."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Copy styles and scripts
    css = generate_css()
    js = generate_js()
    
    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(css)
    with open(os.path.join(output_dir, "app.js"), "w") as f:
        f.write(js)
    
    # Generate homepage
    homepage = generate_homepage(articles)
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(homepage)
    
    # Generate individual article pages
    for article in articles:
        slug = article["url"].rstrip("/").split("/")[-1]
        article_html = generate_article_page(article, articles)
        with open(os.path.join(output_dir, f"{slug}.html"), "w") as f:
            f.write(article_html)
    
    # Generate data file
    with open(os.path.join(output_dir, "data.json"), "w") as f:
        json.dump(articles, f, indent=2)
    
    print(f"Generated {len(articles)} articles in {output_dir}")


def generate_css():
    return """/* AI News — Clean Dark Theme */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');

:root {
  --bg: #0a0a0b;
  --card-bg: #121214;
  --border: #2a2a2e;
  --text: #e8e8ea;
  --text-secondary: #a8a8b0;
  --accent: #8b5cf6;
  --accent-glow: #a897f7;
  --link: #c4b5ff;
  --tag-bg: #1e1e21;
  --tag-text: #c4a8ff;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  line-height: 1.7;
  font-size: 18px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  color: var(--link);
  text-decoration: none;
  transition: opacity 0.2s;
}

a:hover {
  opacity: 0.8;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Header */
header {
  background: rgba(10, 10, 11, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 16px 0;
}

header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo .dot {
  width: 10px;
  height: 10px;
  background: var(--accent);
  border-radius: 50%;
  box-shadow: 0 0 15px var(--accent);
}

nav ul {
  display: flex;
  gap: 32px;
  list-style: none;
}

nav a {
  font-size: 15px;
  font-weight: 500;
  color: var(--text-secondary);
}

nav a:hover {
  color: var(--text);
}

.category-tag {
  display: inline-block;
  background: var(--tag-bg);
  color: var(--tag-text);
  font-size: 13px;
  font-weight: 600;
  padding: 4px 14px;
  border-radius: 20px;
  border: 1px solid var(--border);
  margin-right: 8px;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.featured-badge {
  background: linear-gradient(135deg, var(--accent), #7c3aed);
  color: white;
  font-size: 12px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 16px;
  text-transform: uppercase;
  letter-spacing: 1px;
  display: inline-block;
  margin-bottom: 12px;
}

/* Hero / Featured Article */
.hero {
  margin: 32px 0;
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.hero:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 60px rgba(139, 92, 246, 0.1);
}

.hero-image {
  width: 100%;
  height: 420px;
  object-fit: cover;
  display: block;
}

.hero-content {
  padding: 32px;
}

.hero h1 {
  font-size: 38px;
  font-weight: 800;
  margin-bottom: 16px;
  line-height: 1.2;
  letter-spacing: -0.5px;
}

.hero .meta {
  display: flex;
  align-items: center;
  gap: 16px;
  color: var(--text-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}

.hero .meta span {
  display: flex;
  align-items: center;
  gap: 6px;
}

.hero p {
  font-size: 20px;
  color: var(--text-secondary);
  margin-bottom: 24px;
  max-width: 85ch;
}

/* Article Grid */
.article-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.article-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.3s;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.article-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(139, 92, 246, 0.08);
}

.article-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.article-card .card-content {
  padding: 20px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.article-card h3 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 12px;
  line-height: 1.3;
  flex-grow: 1;
}

.article-card .meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 12px;
}

.article-card .read-more {
  color: var(--accent);
  font-weight: 600;
  font-size: 14px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.article-card .read-more:hover {
  gap: 10px;
}

.read-more::after {
  content: "→";
  transition: transform 0.2s;
}

/* Full-width hero article */
.featured-article {
  position: relative;
  overflow: hidden;
}

.featured-article::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(10, 10, 11, 0.9) 100%);
  z-index: 1;
}

.featured-article img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  filter: brightness(0.7);
}

.featured-article .hero-content {
  position: relative;
  z-index: 2;
  padding: 48px 32px;
  max-width: 800px;
}

.featured-article h1 {
  font-size: 42px;
  color: white;
}

.featured-article p {
  color: #d1d1d6;
  font-size: 18px;
}

/* Article Page */
.article-page {
  max-width: 750px;
  margin: 0 auto;
  padding: 48px 24px;
}

.article-page .category-tag {
  margin-bottom: 16px;
}

.article-page h1 {
  font-size: 42px;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

.article-page .meta {
  display: flex;
  align-items: center;
  gap: 20px;
  color: var(--text-secondary);
  font-size: 15px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
}

.article-page .meta span {
  display: flex;
  align-items: center;
  gap: 8px;
}

.article-page img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  margin: 24px 0;
  display: block;
}

.article-body h2 {
  font-size: 28px;
  font-weight: 700;
  margin: 36px 0 16px;
  color: var(--text);
}

.article-body h3 {
  font-size: 22px;
  font-weight: 600;
  margin: 28px 0 12px;
  color: var(--text);
}

.article-body p {
  margin: 20px 0;
  font-size: 19px;
  line-height: 1.8;
  color: var(--text);
}

.article-body p.lead {
  font-size: 22px;
  font-weight: 300;
  color: var(--text-secondary);
  font-style: italic;
}

.article-body blockquote {
  border-left: 3px solid var(--accent);
  padding: 4px 24px;
  margin: 24px 0;
  font-style: italic;
  color: var(--text-secondary);
}

.article-body ul, .article-body ol {
  margin: 20px 0;
  padding-left: 30px;
}

.article-body li {
  margin: 8px 0;
  font-size: 19px;
}

.article-body a {
  border-bottom: 1px solid var(--link);
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
}

/* Footer */
footer {
  background: rgba(10, 10, 11, 0.8);
  border-top: 1px solid var(--border);
  padding: 48px 0 32px;
  margin-top: 60px;
}

footer .top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
}

footer .logo {
  font-size: 22px;
}

footer .tagline {
  color: var(--text-secondary);
  font-size: 15px;
}

footer .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 32px;
  margin-bottom: 32px;
}

footer h4 {
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

footer ul {
  list-style: none;
}

footer li {
  margin-bottom: 10px;
}

footer a {
  color: var(--text-secondary);
  font-size: 15px;
}

footer a:hover {
  color: var(--link);
}

.copyright {
  text-align: center;
  color: var(--text-secondary);
  font-size: 14px;
  padding-top: 32px;
  border-top: 1px solid var(--border);
}

/* Responsive */
@media (max-width: 768px) {
  .container { padding: 0 16px; }
  nav ul { gap: 16px; }
  .hero h1 { font-size: 28px; }
  .hero .hero-image { height: 280px; }
  .article-grid { grid-template-columns: 1fr; }
  .article-page { padding: 32px 16px; }
  .article-page h1 { font-size: 32px; }
  body { font-size: 17px; }
  .article-body p { font-size: 18px; }
}
"""


def generate_js():
    return """// AI News — Interactive Features
document.addEventListener('DOMContentLoaded', function() {
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Lazy load images
  const images = document.querySelectorAll('img[loading="lazy"]');
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.src = entry.target.dataset.src || entry.target.src;
          entry.target.classList.remove('lazy');
          imageObserver.unobserve(entry.target);
        }
      });
    });
    images.forEach(img => imageObserver.observe(img));
  }

  // Dark mode toggle (respects system preference)
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
  const currentTheme = localStorage.getItem('theme');
  if (currentTheme === 'dark' || (!currentTheme && prefersDark.matches)) {
    document.documentElement.classList.add('dark');
  }
});
"""


def generate_homepage(articles):
    featured = articles[0] if articles else None
    rest = articles[1:] if len(articles) > 1 else []
    
    # Get latest 3
    latest = articles[:3] if articles else []
    
    # Get category unique articles
    by_category = {}
    for a in rest:
        for cat in a.get("categories", []):
            if cat not in by_category:
                by_category[cat] = []
            if len(by_category[cat]) < 3:
                by_category[cat].append(a)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI News — Latest AI News, Insights, and Analysis</title>
  <meta name="description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide.">
  <meta property="og:title" content="AI News — Latest AI News, Insights, and Analysis">
  <meta property="og:description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide.">
  <meta property="og:image" content="https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/voyager-exterior-sign-2-2048x1365.jpg">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo"><span class="dot"></span> AI News</div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="index.html#latest">Latest</a></li>
          <li><a href="index.html#by-category">Categories</a></li>
          <li><a href="index.html#data.json">Data</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <!-- Featured Article -->
    <section class="hero featured-article">
      <img src="{featured['image'] or 'https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/voyager-exterior-sign-2-2048x1365.jpg'}" alt="{featured['title']}" loading="lazy">
      <div class="hero-content">
        <span class="featured-badge">Featured</span>
        {''.join(f'<span class="category-tag">{c}</span>' for c in featured.get('categories', [])[:3])}
        <h1>{featured['title']}</h1>
        <div class="meta">
          <span>By {featured['author']}</span>
          <span>•</span>
          <span>{featured['date']}</span>
        </div>
        <p>{featured['description']}</p>
        <a href="{featured['url'].split('/')[-2] + '-' + featured['url'].split('/')[-1]}.html" class="read-more">Read full story →</a>
      </div>
    </section>

    <!-- Latest Articles -->
    <section id="latest">
      <h2 style="font-size:28px;font-weight:700;margin:32px 0 20px;">Latest News</h2>
      <div class="article-grid">
"""
    
    for article in latest:
        slug = article["url"].split("/")[-2] + "-" + article["url"].split("/")[-1]
        cats = ''.join(f'<span class="category-tag">{c}</span>' for c in article.get("categories", [])[:2])
        html += f"""
        <article class="article-card">
          <img src="{article['image'] or ''}" alt="{article['title']}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{article['title']}</h3>
            <div class="meta">
              <span>{article['date']}</span>
              <span>{article['author']}</span>
            </div>
            <a href="{slug}.html" class="read-more">Read →</a>
          </div>
        </article>
"""
    
    html += """
      </div>
    </section>
"""
    
    # Category sections
    if by_category:
        html += '<section id="by-category">'
        html += '<h2 style="font-size:28px;font-weight:700;margin:32px 0 20px;">By Category</h2>'
        
        for cat, cat_articles in list(by_category.items())[:5]:
            html += f'<h3 style="font-size:20px;font-weight:600;margin:24px 0 16px;color:#a8a8b0;">{cat}</h3>'
            html += '<div class="article-grid">'
            for article in cat_articles:
                slug = article["url"].split("/")[-2] + "-" + article["url"].split("/")[-1]
                cats = ''.join(f'<span class="category-tag">{c}</span>' for c in article.get("categories", [])[:1])
                html += f"""
        <article class="article-card">
          <img src="{article['image'] or ''}" alt="{article['title']}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{article['title']}</h3>
            <div class="meta"><span>{article['date']}</span></div>
            <a href="{slug}.html" class="read-more">Read →</a>
          </div>
        </article>
"""
            html += '</div>'
        
        html += '</section>'
    
    # Footer
    html += """
  </main>

  <footer>
    <div class="container">
      <div class="top">
        <div class="logo"><span class="dot"></span> AI News</div>
        <div class="tagline">Insights powering AI-driven business growth</div>
      </div>
      <div class="grid">
        <div>
          <h4>Categories</h4>
          <ul>
            <li><a href="#">AI Business Strategy</a></li>
            <li><a href="#">AI Startups & Funding</a></li>
            <li><a href="#">AI Hardware & Chips</a></li>
            <li><a href="#">Physical AI</a></li>
            <li><a href="#">AI in Action</a></li>
          </ul>
        </div>
        <div>
          <h4>Resources</h4>
          <ul>
            <li><a href="#">Webinars</a></li>
            <li><a href="#">Whitepapers</a></li>
            <li><a href="#">Reports</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Events</a></li>
          </ul>
        </div>
        <div>
          <h4>Subscribe</h4>
          <p style="color:#a8a8b0;font-size:15px;margin-bottom:12px;">Weekly briefing on AI developments.</p>
          <form id="subscribe-form" style="display:flex;flex-direction:column;gap:8px;">
            <input type="email" placeholder="Your email" required style="padding:10px 14px;border:1px solid var(--border);border-radius:8px;background:#0a0a0b;color:var(--text);font-size:15px;">
            <button type="submit" style="padding:10px;border:none;border-radius:8px;background:var(--accent);color:white;font-weight:600;cursor:pointer;font-size:15px;">Subscribe</button>
          </form>
        </div>
      </div>
      <div class="copyright">
        &copy; 2026 AI News. All rights reserved.
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
  <script>
    document.getElementById('subscribe-form')?.addEventListener('submit', function(e) {
      e.preventDefault();
      const email = this.querySelector('input[type="email"]').value;
      if (email) {
        alert('Thank you for subscribing! You will receive our weekly AI briefing.');
        this.reset();
      }
    });
  </script>
</body>
</html>
"""
    return html


def generate_article_page(article, all_articles):
    slug = article["url"].split("/")[-2] + "-" + article["url"].split("/")[-1]
    related = [a for a in all_articles if a["url"] != article["url"]][:4]
    
    cats = ''.join(f'<span class="category-tag">{c}</span>' for c in article.get("categories", []))
    tags = ''.join(f'<a href="#" style="color:var(--tag-text);font-size:13px;background:var(--tag-bg);padding:4px 12px;border-radius:12px;border:1px solid var(--border);">{t}</a>' for t in article.get("tags", [])[:10])
    
    # Split body into paragraphs
    body_paragraphs = article.get("body", "").split("\n\n")
    body_html = ""
    for i, para in enumerate(body_paragraphs[:30]):
        if para.startswith("## "):
            body_html += f'<h2>{para[3:]}</h2>\n'
        elif para.startswith("### "):
            body_html += f'<h3>{para[4:]}</h3>\n'
        elif para.startswith("• "):
            body_html += f'<li>{para[2:]}</li>\n'
        elif len(para.strip()) > 10:
            cls = ' class="lead"' if i == 0 else ''
            body_html += f'<p{cls}>{para.strip()}</p>\n'
    
    related_html = ""
    for rel in related:
        rel_slug = rel["url"].split("/")[-2] + "-" + rel["url"].split("/")[-1]
        related_html += f"""
        <article class="article-card">
          <img src="{rel['image'] or ''}" alt="{rel['title']}" loading="lazy">
          <div class="card-content">
            <h3 style="font-size:17px;">{rel['title']}</h3>
            <div class="meta" style="font-size:13px;">
              <span>{rel['date']}</span>
            </div>
            <a href="{rel_slug}.html" class="read-more">Read →</a>
          </div>
        </article>
"""
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{article['title']} — AI News</title>
  <meta name="description" content="{article['description'][:160]}">
  <meta property="og:title" content="{article['title']}">
  <meta property="og:description" content="{article['description'][:160]}">
  <meta property="og:image" content="{article['image'] or ''}">
  <meta property="og:type" content="article">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo"><a href="index.html" style="color:inherit;text-decoration:none;"><span class="dot"></span> AI News</a></div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="index.html#latest">Latest</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <article class="article-page">
    {cats}
    <h1>{article['title']}</h1>
    <div class="meta">
      <span>By {article['author']}</span>
      <span>•</span>
      <span>{article['date']}</span>
    </div>
    
    <img src="{article['image'] or ''}" alt="{article['title']}" loading="lazy">
    
    <div class="article-body">
      {body_html}
    </div>
    
    <div class="tags">
      {tags}
    </div>
  </article>

  <section class="container" style="margin-top:48px;">
    <h2 style="font-size:24px;font-weight:700;margin-bottom:20px;">Related Articles</h2>
    <div class="article-grid">
      {related_html}
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="top">
        <div class="logo"><span class="dot"></span> AI News</div>
        <div class="tagline">Insights powering AI-driven business growth</div>
      </div>
      <div class="copyright">
        &copy; 2026 AI News. All rights reserved.
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    print("=" * 60)
    print("AI News Scraper & Site Generator")
    print("=" * 60)
    print()
    
    # Check for cached data
    cache_file = "data.json"
    
    print("Scraping latest articles from AI-News.com...")
    print("This will take 30-60 seconds...")
    print()
    
    articles = scrape_all()
    
    if articles:
        print(f"\nSuccessfully scraped {len(articles)} articles")
        for a in articles:
            print(f"  - {a['title'][:70]}..." if len(a['title']) > 70 else f"  - {a['title']}")
        
        print("\nGenerating site...")
        generate_site(articles, "site")
        print("\nDone! Site generated in ./site/")
    else:
        print("No articles scraped. Check network or site structure.")
