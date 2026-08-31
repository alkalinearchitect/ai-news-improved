#!/usr/bin/env python3
"""
AI News - World-Class Static Site Generator v3
Swiss/Modernist design: pure black canvas, serif headlines, sans body
Custom Flux-generated images, zero glow/shadow/gradients
"""

import json
import os
import re
import html

from article_data import ARTICLE_BODIES


# ============================================================================
# Article metadata (bodies loaded from article_data.py)
# ============================================================================

ARTICLES = [
    {
        "url": "nvidia-circular-financing-ai-labs",
        "title": "A quarter of Nvidia's business next year comes from labs it is financing",
        "author": "Dashveenjit Kaur",
        "date": "August 27, 2026",
        "desc": "Nvidia has put nearly US$50 billion into the AI labs that buy its chips, and has lined up commitments for more than $500 billion in circular financing.",
        "image": "images/nvidia-financing.jpg",
        "tags": ["agentic ai", "ai infrastructure", "ai investment", "nvidia", "openai"],
        "cats": ["AI Business Strategy", "AI Hardware", "Artificial Intelligence"],
    },
    {
        "url": "gatik-200m-ai-autonomous-freight",
        "title": "Gatik raises $200M to scale AI-powered autonomous freight",
        "author": "Muhammad Zulhusni",
        "date": "August 26, 2026",
        "desc": "Autonomous trucking company Gatik has raised $200 million in Series D funding to expand driverless freight across North America.",
        "image": "images/gatik-truck.jpg",
        "tags": ["autonomous vehicles", "logistics", "physical ai", "startups"],
        "cats": ["AI Startups", "Funding", "Physical AI", "Retail Logistics"],
    },
    {
        "url": "nvidia-jetson-orin-nano-2",
        "title": "NVIDIA Jetson Orin Nano 2 brings physical AI to drones and robots",
        "author": "Ryan Daws",
        "date": "August 26, 2026",
        "desc": "NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer bringing physical AI to drones, robots, and vision systems.",
        "image": "images/jetson-edge.jpg",
        "tags": ["ai hardware", "computer vision", "drones", "edge ai", "robotics"],
        "cats": ["AI Hardware", "Computer Vision", "Physical AI"],
    },
    {
        "url": "mit-ai-forecasts-extreme-weather",
        "title": "MIT AI forecasts extreme weather without historical data",
        "author": "Ryan Daws",
        "date": "August 25, 2026",
        "desc": "MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.",
        "image": "images/mit-weather.jpg",
        "tags": ["weather forecasting", "machine learning", "mit", "risk assessment"],
        "cats": ["Environment", "Government AI", "Data Engineering"],
    },
    {
        "url": "xpeng-iron-humanoid-robot",
        "title": "XPENG IRON humanoid robot draws record physical AI funding",
        "author": "Ryan Daws",
        "date": "August 24, 2026",
        "desc": "XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.",
        "image": "images/xpeng-robot.jpg",
        "tags": ["humanoid", "robots", "xpeng", "funding"],
        "cats": ["AI Hardware", "AI Startups", "Physical AI", "Robotics"],
    },
    {
        "url": "stripe-openrouter-acquisition",
        "title": "Stripe agrees to buy OpenRouter as AI model routing expands",
        "author": "Muhammad Zulhusni",
        "date": "August 20, 2026",
        "desc": "Stripe has agreed to acquire OpenRouter, an AI model-routing platform giving developers access to hundreds of models through a single API.",
        "image": "images/stripe-openrouter.jpg",
        "tags": ["ai infrastructure", "api", "mergers & acquisitions"],
        "cats": ["AI Business Strategy", "AI Market Trends", "AI Mergers"],
    },
    {
        "url": "amazons-prime-air-drones",
        "title": "Amazon's Prime Air autonomous drones to reach 500 US cities",
        "author": "Ryan Daws",
        "date": "August 20, 2026",
        "desc": "Amazon plans to expand Prime Air drone delivery to nearly 500 cities across the US by end of 2026.",
        "image": "images/amazon-drones.jpg",
        "tags": ["drone delivery", "amazon", "logistics", "physical ai"],
        "cats": ["AI in Action", "Computer Vision", "Physical AI"],
    },
    {
        "url": "agentic-ai-in-government-uae",
        "title": "Agentic AI in government: deciding what a machine may decide",
        "author": "Staff Writer",
        "date": "August 20, 2026",
        "desc": "The UAE becomes first jurisdiction to formally classify and regulate agentic AI systems in public-sector operations.",
        "image": "images/agentic-ai.jpg",
        "tags": ["agentic ai", "government", "regulation", "uae"],
        "cats": ["AI in Action", "AI and Us"],
    },
]

# Attach bodies
for a in ARTICLES:
    a["body"] = ARTICLE_BODIES.get(a["url"], "")


# ============================================================================
# Design constants
# ============================================================================

FONTS_LINK = (
    '<link href="https://fonts.googleapis.com/css2'
    '?family=Inter:wght@300;400;500;600;700'
    '&family=Crimson+Text:wght@300;400;600;700&display=swap" '
    'rel="stylesheet">'
)

# Load CSS and JS from files written separately
CSS = open("docs/style.css").read() if os.path.exists("docs/style.css") else ""
JS = open("docs/app.js").read() if os.path.exists("docs/app.js") else ""

BASE_URL = "https://alkalinearchitect.github.io/ai-news-improved/"


def h(text):
    return html.escape(str(text))


def render_cats(cats, max_n=3):
    if not cats:
        return ""
    return "".join(f'<span class="category-tag">{h(c)}</span>' for c in cats[:max_n])


def render_tags(tags):
    if not tags:
        return ""
    return "".join(f'<a href="#">{h(t)}</a>' for t in tags[:12])


def render_body(body_text):
    if not body_text:
        return "<p>No content available.</p>"
    parts = body_text.strip().split("\n\n")
    html_parts = []
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if part.startswith("## "):
            html_parts.append(f"<h2>{h(part[3:])}</h2>")
        elif part.startswith("### "):
            html_parts.append(f"<h3>{h(part[4:])}</h3>")
        elif part.startswith("1. "):
            items = part.split("\n")
            html_parts.append("<ol>")
            for item in items:
                line = item.strip()
                if line and re.match(r'\d+\.\s', line):
                    clean = re.sub(r'^\d+\.\s', '', line)
                    html_parts.append(f"<li>{h(clean)}</li>")
            html_parts.append("</ol>")
        elif part.startswith("  - "):
            items = part.split("\n")
            html_parts.append("<ul>")
            for item in items:
                line = item.strip()
                if line.startswith("- "):
                    html_parts.append(f"<li>{h(line[2:])}</li>")
            html_parts.append("</ul>")
        elif part.startswith("- "):
            items = part.split("\n")
            html_parts.append("<ul>")
            for item in items:
                line = item.strip()
                if line.startswith("- "):
                    html_parts.append(f"<li>{h(line[2:])}</li>")
            html_parts.append("</ul>")
        else:
            cls = ' class="lead"' if i == 0 else ''
            text = h(part)
            html_parts.append(f"<p{cls}>{text}</p>")
    return "\n".join(html_parts)


def gen_homepage():
    featured = ARTICLES[0]
    latest = ARTICLES[:7]
    
    # Group by category (deduplicated)
    by_cat = {}
    seen = set()
    for a in latest[1:]:
        for cat in a.get("cats", []):
            if cat not in by_cat:
                by_cat[cat] = []
            if a["url"] not in seen and len(by_cat[cat]) < 3:
                by_cat[cat].append(a)
                seen.add(a["url"])
    
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI News - Latest AI News, Insights, and Analysis</title>
  <meta name="description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide. No cookie walls, no paywalls.">
  <meta property="og:title" content="AI News - Latest AI News, Insights, and Analysis">
  <meta property="og:description" content="AI News delivers the latest updates in AI, machine learning, and emerging tech worldwide. No cookie walls, no paywalls.">
  <meta property="og:image" content="{BASE_URL}{featured['image']}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="index,follow">
  {FONTS_LINK}
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
      <nav>
        <ul>
          <li><a href="index.html" class="active">Home</a></li>
          <li><a href="#latest">Latest</a></li>
          <li><a href="#by-category">Categories</a></li>
          <li><a href="data.json">API</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <img src="{featured['image']}" alt="{h(featured['title'])}" class="hero-image" loading="lazy">
      <div class="hero-content">
        <span class="featured-badge">Featured</span>
        {render_cats(featured.get('cats', []))}
        <h1>{h(featured['title'])}</h1>
        <div class="meta">
          <span class="byline">By {h(featured['author'])}</span>
          <span>&bull;</span>
          <span class="date">{h(featured['date'])}</span>
        </div>
        <p class="excerpt">{h(featured['desc'])}</p>
        <a href="{featured['url']}.html" class="read-more">Read full story</a>
      </div>
    </section>

    <section id="latest">
      <h2 class="section-title">Latest</h2>
      <div class="article-grid">
"""
    
    for article in latest[1:]:
        cats = render_cats(article.get("cats", []), 2)
        img = article.get("image", "")
        out += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{h(article['title'])}</h3>
            <div class="card-meta">
              <span class="date">{h(article['date'])}</span>
              <span class="byline">{h(article['author'])}</span>
            </div>
            <a href="{article['url']}.html" class="read-more-small">Read</a>
          </div>
        </article>
"""
    
    out += "\n      </div>\n    </section>\n"
    
    # Category sections
    out += '<section id="by-category">'
    out += '<h2 class="section-title">By Category</h2>'
    
    for cat, cat_articles in list(by_cat.items())[:5]:
        out += f'<h3>{h(cat)}</h3>'
        out += '<div class="article-grid">'
        for article in cat_articles:
            cats = render_cats(article.get("cats", []), 1)
            img = article.get("image", "")
            out += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{h(article['title'])}</h3>
            <div class="card-meta">
              <span class="date">{h(article['date'])}</span>
            </div>
            <a href="{article['url']}.html" class="read-more-small">Read</a>
          </div>
        </article>
"""
        out += '</div>'
    
    out += '</section>'
    
    # Subscribe
    out += """
    <section>
      <div class="subscribe-box">
        <h3>Daily Brief</h3>
        <p>The latest AI news, curated and delivered to your inbox. No spam, no cookie walls.</p>
        <form id="subscribe-form">
          <input type="email" placeholder="you@domain.com" required>
          <button type="submit">Subscribe</button>
        </form>
      </div>
    </section>
"""
    
    # Footer
    out += """
  </main>

  <footer>
    <div class="container">
      <div class="top">
        <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
        <span class="tagline">Insights at the intersection of technology and society</span>
      </div>
      <div class="grid">
        <div>
          <h4>Categories</h4>
          <ul>
            <li><a href="#">AI Business Strategy</a></li>
            <li><a href="#">AI Startups & Funding</a></li>
            <li><a href="#">AI Hardware</a></li>
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
        alert('Thank you for subscribing!');
        this.reset();
      }
    });
  </script>
</body>
</html>
"""
    return out


def gen_article(article, all_articles):
    related = [a for a in all_articles if a["url"] != article["url"]][:4]
    cats = render_cats(article.get("cats", []))
    tags = render_tags(article.get("tags", []))
    body_html = render_body(article["body"])
    
    related_html = ""
    for rel in related:
        img = rel.get("image", "")
        rel_cats = render_cats(rel.get("cats", []), 1)
        related_html += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(rel['title'])}" loading="lazy">
          <div class="card-content">
            {rel_cats}
            <h3>{h(rel['title'])}</h3>
            <div class="card-meta">
              <span class="date">{h(rel['date'])}</span>
            </div>
            <a href="{rel['url']}.html" class="read-more-small">Read</a>
          </div>
        </article>
"""
    
    img_tag = ""
    if article.get("image"):
        img_tag = f'<img src="{article["image"]}" alt="{h(article["title"])}" loading="lazy">'
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{h(article['title'])} - AI News</title>
  <meta name="description" content="{h(article['desc'][:160])}">
  <meta property="og:title" content="{h(article['title'])}">
  <meta property="og:description" content="{h(article['desc'][:160])}">
  <meta property="og:image" content="{BASE_URL}{article.get('image', '')}">
  <meta property="og:type" content="article">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="index,follow">
  {FONTS_LINK}
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
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
    <h1>{h(article['title'])}</h1>
    <div class="meta">
      <span class="byline">By {h(article['author'])}</span>
      <span>&bull;</span>
      <span class="date">{h(article['date'])}</span>
    </div>
    {img_tag}
    <div class="article-body">
      {body_html}
    </div>
    <div class="tags">
      {tags}
    </div>
  </article>

  <section class="container" style="margin-top:56px;">
    <h2 class="section-title">Related</h2>
    <div class="article-grid">
      {related_html}
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="top">
        <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
        <span class="tagline">Insights at the intersection of technology and society</span>
      </div>
      <div class="copyright">
        &copy; 2026 AI News. All rights reserved.
      </div>
    </div>
  </footer>
  <script src="app.js"></script>
</body>
</html>"""


def generate_site():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)
    
    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(CSS)
    
    with open(os.path.join(output_dir, "app.js"), "w") as f:
        f.write(JS)
    
    # Clean up old/duplicate files
    for f_name in list(os.listdir(output_dir)):
        f_path = os.path.join(output_dir, f_name)
        if os.path.isfile(f_path) and f_name.endswith(".html"):
            # Keep index.html and files matching article slugs
            if f_name != "index.html" and f_name not in [f"{a['url']}.html" for a in ARTICLES]:
                os.remove(f_path)
    
    # Write new files
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(gen_homepage())
    
    for article in ARTICLES:
        with open(os.path.join(output_dir, f"{article['url']}.html"), "w") as f:
            f.write(gen_article(article, ARTICLES))
    
    # Write data.json
    with open(os.path.join(output_dir, "data.json"), "w") as f:
        json.dump(ARTICLES, f, indent=2)
    
    print(f"Generated {len(ARTICLES) + 1} pages (1 homepage + {len(ARTICLES)} articles)")
    for f_name in sorted(os.listdir(output_dir)):
        f_path = os.path.join(output_dir, f_name)
        if os.path.isfile(f_path):
            size = os.path.getsize(f_path)
            print(f"  {f_name} ({size:,} bytes)")
    img_dir = os.path.join(output_dir, "images")
    if os.path.isdir(img_dir):
        imgs = os.listdir(img_dir)
        total = sum(os.path.getsize(os.path.join(img_dir, f)) for f in imgs)
        print(f"  images/ ({len(imgs)} files, {total:,} bytes)")


if __name__ == "__main__":
    print("=" * 60)
    print("AI News - World-Class Site Generator v3")
    print("Swiss/Modernist | Serif headlines | Custom Flux images")
    print("=" * 60)
    print()
    generate_site()
