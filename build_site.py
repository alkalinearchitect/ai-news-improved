#!/usr/bin/env python3
"""
AI News — World-Class Static Site Generator
Built by OWL using Swiss/modernist design language.

Design principles (non-negotiable):
- Pure black canvas #000, near-black #070708 text
- Editorial serif display headlines (Georgia, Iowan, Palatino)
- System sans body (Inter, Helvetica, Arial)
- Mono for metadata (SFMono, Menlo)
- Zero box-shadow, zero radial gradient glow
- Hairline 1px borders only
- Accent violet #8b5cf6 ONLY for functional punctuation
- Custom AI-generated images via Flux (no stock photo scraping)
- No cookie wall, no sponsor banners, no ad interruptions
"""

import json
import os
import re
import html


# ============================================================================
# ARTICLE DATA (scraped from AI-News.com, latest Aug 2026)
# ============================================================================

ARTICLES = [
    {
        "url": "https://www.artificialintelligence-news.com/news/nvidia-circular-financing-ai-labs/",
        "slug": "nvidia-circular-financing-ai-labs",
        "title": "A quarter of Nvidia's business next year comes from labs it is financing",
        "author": "Dashveenjit Kaur",
        "date": "August 27, 2026",
        "description": "Nvidia has put nearly US$50 billion into the AI labs that buy its chips, and has lined up commitments for more than $500 billion. The arrangement is what people mean by circular financing.",
        "image": "images/nvidia-financing.jpg",
        "tags": ["agentic ai", "ai infrastructure", "ai investment", "colette kress", "data centres", "earnings", "nvidia", "openai"],
        "categories": ["AI Business Strategy", "AI Hardware", "Artificial Intelligence", "Inside AI", "Physical AI"],
        "body": """Nvidia has put nearly US$50 billion into the AI labs that buy its chips, and has lined up commitments for more than $500 billion.

Colette Kress, the company's chief financial officer, told analysts on August 26 that demand from the labs Nvidia backs with its own balance sheet will contribute toward roughly a quarter of its business next year.

That arrangement is what people mean by circular financing, and Nvidia used the phrase before any analyst did. Kress said on the earnings call that the company recognised the scale of the support it was providing and knew some would call it circular financing. She said Nvidia sees it differently.

The loop is simple to describe. Nvidia invests in an AI lab. The lab uses the money, or the credit Nvidia's involvement unlocks, to build a data centre. The data centre is filled with Nvidia chips. The purchase is recorded as Nvidia revenue. Nvidia's share price and cash pile grow, and it invests again.

## What Nvidia has committed

Kress gave the figures herself. She said Nvidia has signed partnerships with six investment firms, naming Apollo Global Management, BlackRock, Blackstone, Brookfield Asset Management, Goldman Sachs and KKR, to set up financing platforms that will raise more than $500 billion of outside capital for the labs to build with.

She said Nvidia secured land, power and building capacity with SB Energy that will host only Nvidia equipment. The first phase supports 4.25 gigawatts and will be used by OpenAI. Kress put OpenAI's existing and planned commitments at around 12 gigawatts of Nvidia compute through 2030. For a second lab she did not name, Nvidia will provide credit support covering nearly two gigawatts.

Nvidia's results statement describes those partnerships as subject to definitive agreements, which means the binding contracts have not been signed. The $500 billion is an intention rather than money in place.

## Why Nvidia rejects the circular financing label

Kress gave three answers, and they deserve to be reported alongside the numbers.

Outside lenders still assess every deal on its own merits, she said, and Nvidia is not making loans. The chips Nvidia ships go to customers that are investment grade or backed by someone who is. And if a customer does fail, the equipment can be moved to another buyer, which she offered as the reason Nvidia's exposure is limited.

Kress also explained why the labs need the help. They have more demand for computing than their finances can support, she said. They are young companies without the long contracts and credit ratings that lenders normally require before funding a data centre. What limits their growth is not customers or technology. It is access to computing.

The obvious risk is what happens if one of them cannot pay. Nvidia would lose the sale and the investment at the same time. Kress answers that the hardware finds another buyer. That claim only holds while demand exceeds supply, and Nvidia says it currently does.

Vivek Arya of BofA Securities asked Jensen Huang how the company squares funding labs that are designing their own chips, pointing to OpenAI's Jalapeño processor. Huang said Nvidia sells a platform that works in any cloud across the whole life of an AI system, while rival chips are built for one service. On the money, he said his only regret was not investing more and sooner.

## The agent assumption underneath it all

Kress told Morgan Stanley's Joseph Moore that an agent needs somewhere between 15 and 100 times the computing power of a person using the same system. Huang said he believes AI tipped over to being mostly agentic in the past month. Nvidia offered no data for that.

On that basis, the company guided to $108 billion in revenue this quarter and said it preliminarily expects around 70% growth in the year to January 2028, a figure Kress said is limited by supply rather than demand.

Kress separately warned that memory prices are climbing faster than Nvidia expected. She guided margins down to 74% this quarter, bottoming at 71% to 72% in the fourth, and said memory scarcity is being driven in large part by the AI buildout itself."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/gatik-200m-ai-autonomous-freight/",
        "slug": "gatik-200m-ai-autonomous-freight",
        "title": "Gatik raises $200M to scale AI-powered autonomous freight",
        "author": "Muhammad Zulhusni",
        "date": "August 26, 2026",
        "description": "Autonomous trucking company Gatik has raised $200 million in Series D funding to expand its driverless freight operations across North America.",
        "image": "images/gatik-truck.jpg",
        "tags": ["ai", "autonomous vehicles", "logistics", "physical ai", "retail automation", "startups"],
        "categories": ["AI in Action", "AI Startups", "Funding", "Artificial Intelligence", "Physical AI", "Retail Logistics"],
        "body": """Autonomous trucking company Gatik has raised $200 million in Series D funding to expand its driverless freight operations across North America. The round was led by Qatar Investment Authority and Koch Disruptive Technologies, with participation from Millennium Management, ARK Invest, Intact Private Capital, and other investors.

Gatik said it has more than $600 million in contracted revenue and has completed 85,000 fully driverless orders. The company reported a 99% on-time delivery rate across its operations.

Its trucks currently move goods between distribution centres and stores across regional networks in Texas, Arizona, Arkansas, and Canada. Gatik operates dozens of fully driverless trucks and says it plans to expand the fleet to thousands over the coming years.

A Gatik spokesperson told Reuters that the company is targeting more than 100 driverless trucks by the end of 2026. Gatik plans to use the new capital to expand commercial operations and its fleet while continuing to invest in technology, infrastructure, and its workforce.

## From fixed routes to dynamic freight networks

Gatik's autonomous vehicle system is designed for regional freight routes covering highways and surface streets. Gatik describes Gatik Driver as its proprietary AI system for autonomous freight. The company's fully driverless trucks operate without a human driver or safety observer on board.

When Gatik and Loblaw announced their initial Toronto fleet in 2020, five vehicles were scheduled to operate on five predetermined routes with fixed pickup and drop-off locations.

By 2022, Gatik's fully driverless Loblaw operation was transporting ambient, refrigerated, and frozen goods from a distribution facility to five nearby stores. Loblaw described the routes as fixed, repetitive, and predictable.

PepsiCo said Gatik's newer deployments can operate across highways and surface streets using dynamic route orchestration for networks spanning hundreds of pickup and drop-off locations.

PepsiCo said route plans can be adjusted by adding or removing stops, responding to shifts in demand, and adapting to activity at distribution centres. The company said these changes can be made within its existing transportation operations without requiring major alterations to the network.

TechCrunch reported that Gatik began with fixed trips of less than 10 miles but now operates dynamic routes containing dozens of pickup and drop-off points and covering distances of up to 400 miles.

## Scaling AI and autonomous truck production

Gatik also uses simulation and synthetic data to develop and validate its autonomous driving software. In July 2025, the company introduced Arena, an internally developed simulation platform designed to reproduce driving environments without relying exclusively on physical road testing.

Arena generates structured synthetic data that can be used to test autonomous driving behaviour across different conditions. The platform is designed to reproduce routine situations as well as rare or high-risk scenarios that are harder to encounter repeatedly during real-world testing.

Arena incorporates Nvidia Cosmos world foundation models to generate synthetic driving environments used for training and validation.

Isuzu Motors invested $30 million in Gatik in 2024 as part of a partnership to develop Level 4 autonomous commercial vehicles in North America. The companies are jointly developing a redundant chassis designed for autonomous driving."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/nvidia-jetson-orin-nano-2-physical-ai-to-drones-and-robots/",
        "slug": "nvidia-jetson-orin-nano-2-physical-ai-to-drones-and-robots",
        "title": "NVIDIA Jetson Orin Nano 2 brings physical AI to drones and robots",
        "author": "Ryan Daws",
        "date": "August 26, 2026",
        "description": "NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer aimed at bringing physical AI to drones, robots, and vision systems.",
        "image": "images/jetson-edge.jpg",
        "tags": ["ai hardware", "computer vision", "drones", "edge ai", "jetson orin", "multimodal", "nvidia", "physical ai", "robotics", "tensor cores"],
        "categories": ["AI Hardware", "Computer Vision", "Featured", "How It Works", "Infrastructure", "Physical AI", "Retail Logistics"],
        "body": """NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer aimed at bringing physical AI to drones, robots, and vision systems. The company is positioning the new board as an entry-level option for developers who want generative AI models running directly on a machine instead of inside a data centre.

NVIDIA's argument for the launch rests on a change in how well small and medium AI models now perform. The company says models of this size have reached the accuracy that only the largest frontier models achieved a year earlier.

"Deepu Talla, VP of Robotics and Edge AI at NVIDIA, said: The Jetson Orin Nano 2 computer puts that breakthrough within reach of millions of developers, delivering the performance and energy efficiency needed for real-time reasoning at the edge."

Achieving that level of accuracy from small and medium AI models lets compact edge hardware interpret language and images and act on that information in real-time. Robots, delivery drones, inspection drones, and vision AI systems all depend on hardware that can run those workloads without drawing much power.

## Compute specs and power draw

Jetson Orin Nano 2 carries 78 trillion operations per second of AI compute, 8GB of memory, and an eight-core Arm CPU. NVIDIA built the board to deliver a jump in AI and video-processing performance while keeping cost and power draw low.

The new board reaches twice the inference performance of the existing Jetson Orin Nano Super. NVIDIA attributes that gain to improved Tensor Cores and higher memory bandwidth, packed inside the same compact form factor as its predecessor. Running in 15-watt mode, Jetson Orin Nano 2 uses 40 percent less power than the Orin Nano Super while matching its performance level.

Jetson Orin Nano 2 runs on NVIDIA's open software stack alongside Jetson agent skills and the wider Jetson AI ecosystem. The company names its own Cosmos and Nemotron models as examples, alongside Gemma 4 and Qwen 3, as models developers can deploy on the hardware.

## Early partners test physical AI applications

Cognex, Doosan Bobcat, and Matic sit among the first companies NVIDIA names as adopting and exploring Jetson Orin Nano 2. NVIDIA says more than three million developers already build on its robotics stack.

Wing, the drone delivery subsidiary of Alphabet, already runs Jetson Orin Nano Super and NVIDIA's software stack across its delivery drone fleet. The company plans to evaluate Jetson Orin Nano 2 to push further into real-time AI perception and reasoning.

Matic Robots, a consumer robotics company, is adopting Jetson Orin Nano 2 for its home cleaning robots. NVIDIA says the board will let Matic add conversational AI, gesture detection, precision mapping and semantic understanding of the home, alongside autonomous cleaning behaviour.

Frontier intelligence has reached the edge. Frontier models that used to run inside data centers last year can now run in real time on entry-level Jetson systems."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/mit-ai-forecasts-extreme-weather-without-historical-data/",
        "slug": "mit-ai-forecasts-extreme-weather-without-historical-data",
        "title": "MIT AI forecasts extreme weather without historical data",
        "author": "Ryan Daws",
        "date": "August 25, 2026",
        "description": "MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.",
        "image": "images/mit-weather.jpg",
        "tags": ["disaster planning", "flood prediction", "infrastructure", "machine learning", "mit", "predictive modelling", "risk assessment", "weather forecasting"],
        "categories": ["AI in Action", "Data Engineering", "Deep Dives", "Environment", "Featured", "Government AI", "Utilities"],
        "body": """MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.

Kai Chang, a mechanical engineering graduate student, and Professor Themis Sapsis developed the tool. It produces maps of events that have not appeared in a region's historical record but remain statistically-possible. Each map also carries estimates of the event's likely duration and intensity, alongside a separate estimate of the area it might affect.

## Forecasting extreme weather events without historical precedent

Sapsis holds the William I. Koch Professorship in Mechanical and Ocean Engineering at MIT. Both researchers are affiliated with the MIT Center for Computational Science and Engineering, and Sapsis also holds an appointment with the MIT Institute for Data, Systems, and Society. The pair describe the method, named Extreme Event Aware or eta-learning, in a paper published in Nature Communications on 20 August.

Existing risk models work differently. Insurers, city planners, and grid operators typically want to know what a once-in-a-century storm might look like for a specific location. Current simulations usually depend on datasets that already contain extreme events, learning the conditions that produced them before projecting similar patterns forward.

Chang argues this current approach creates a limit on what such models can show. These methods assume there are very disastrous events that we have seen in the dataset, and they build a method to either estimate the risk of those events, or they try to predict exactly the events that have happened.

Sapsis frames the same limitation through Hurricane Katrina. An event like Hurricane Katrina is something that happens every 30 to 40 years. What will be the Katrina that happens every 100 years? How bad will it be? That is exactly what we are trying to quantify, to help planners prepare for plausible extreme scenarios.

## Combining point statistics with spatial detail

The algorithm works from two types of data. Point statistics capture how often a given intensity level, such as the maximum rainfall recorded across a map, occurs within a dataset. Spatial maps show how an event's impact varies across a region.

Learning the statistical relationship between the two lets the algorithm build spatial patterns for events beyond anything in its training data, without needing prior examples of those exact extremes.

The researchers tested the approach on precipitation across the continental US. They started with 25 years of hourly rainfall data, pooled into daily maps, and computed point statistics describing how often the maximum rainfall on a map reached a given level across that full record.

## Testing infrastructure against worst-case maps

The highest rainfall ever recorded in New York City measures 200 millimetres. The method can generate plausible maps of a storm that produces 300 millimetres instead, a level with no match in the observational record.

A user can prompt the trained algorithm to show what a once-in-a-century storm might look like for a named city. The output takes the form of maps showing statistically-plausible storms at that frequency.

The generated maps could help a city test its seawall against a storm surge beyond anything recorded. The same maps could show whether the power grid would hold during a longer heatwave, or whether firefighting resources could contain a wildfire larger than any on file.

## Limits of the demonstration so far

Applying the method to a new hazard requires relevant point statistics and spatial data for that specific hazard. The pair point to possible extensions once that data is available.

Sapsis notes that global infrastructure has been optimised for efficiency, leaving little slack in the systems it supports. A single extreme event propagates through supply chains, energy markets, and food systems in weeks. Being able to put a probability on an event that has not happened yet is now a question of national and economic resilience.

The paper was published in Nature Communications on 20 August 2026."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/xpeng-iron-humanoid-robot-draws-record-physical-ai-funding/",
        "slug": "xpeng-iron-humanoid-robot-draws-record-physical-ai-funding",
        "title": "XPENG IRON humanoid robot draws record physical AI funding",
        "author": "Ryan Daws",
        "date": "August 24, 2026",
        "description": "XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.",
        "image": "images/xpeng-robot.jpg",
        "tags": ["alibaba", "funding", "he xiaopeng", "humanoid", "idg capital", "physical ai", "robotics", "robots", "tencent", "venture capital", "xpeng"],
        "categories": ["AI Hardware", "AI in Action", "AI Market Trends", "AI Startups", "Featured", "Founders", "Manufacturing", "Physical AI", "World of Work"],
        "body": """XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.

The Chinese electric vehicle maker announced the funding round for its robotics business through a set of share purchase agreements with multiple investors. XPENG says the deal represents the largest single-round private capital raise in China's physical AI industry to date.

He Xiaopeng, Chairman and CEO of XPENG, said: Over the past 12 years, XPENG has remained committed to full-stack in-house R&D, building a solid technological foundation for the physical AI era.

This has enabled us to pioneer a new phase of mass production and commercial deployment for advanced humanoid robots.

## IDG Capital leads the round

IDG Capital led the financing round, with Gaorong Ventures also participating as an investor. Tencent and Alibaba joined as strategic investors. XPENG will keep controlling ownership of the robotics business once the round closes.

XPENG said the capital will fund long-term investment in full-stack physical AI development. The company also plans to use the raise to strengthen incentive arrangements for senior executives and other staff working on robotics.

## Inside IRON, XPENG's humanoid robot platform

IRON is at the centre of XPENG's physical AI strategy. The humanoid robot uses a fully-enclosed flexible lattice structure that XPENG designed in-house to balance appearance with safety. IRON has 76 degrees of freedom across its body and 21 in each hand.

XPENG built the robot's hardware platform itself, including the chips and controllers that drive the robot's core movement systems. Separate motion modules and dexterous hand mechanisms handle finer manipulation tasks.

On compute, XPENG puts IRON's combined output at up to 2,250 TOPS of effective computing power, delivered across three in-house-designed Turing AI chips. That on-board processing lets XPENG run its physical AI foundation model directly on the robot.

XPENG argues that IRON's human-like hardware gives it an advantage in collecting behavioural data from everyday human activity, and in adapting to environments and tools built for people.

IRON is expected to enter mass production by the end of 2026. Initial deployment will happen inside the company's own stores and campuses before any wider rollout. XPENG plans to begin deliveries to customers in China and overseas markets during 2027.

## Investors point to XPENG's physical AI manufacturing scale

IDG Capital said the physical AI industry is moving from technical breakthroughs to scalable manufacturing and commercial deployment. The firm pointed to XPENG's combination of edge AI processors, physical AI foundation models, and complete robotic systems.

IRON is expected to enter mass production by the end of 2026, with customer deliveries planned for 2027 across China and overseas markets."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/stripe-openrouter-acquisition-ai-model-routing/",
        "slug": "stripe-openrouter-acquisition-ai-model-routing",
        "title": "Stripe agrees to buy OpenRouter as AI model routing expands",
        "author": "Muhammad Zulhusni",
        "date": "August 20, 2026",
        "description": "Stripe has agreed to acquire OpenRouter, an AI model-routing platform that gives developers access to hundreds of models through a single interface.",
        "image": "images/stripe-openrouter.jpg",
        "tags": ["ai", "ai infrastructure", "api", "aws bedrock", "developers", "mergers & acquisitions"],
        "categories": ["AI Business Strategy", "AI Market Trends", "AI Mergers", "Artificial Intelligence", "Featured", "Infrastructure", "Inside AI"],
        "body": """Stripe has agreed to acquire OpenRouter, an AI model-routing platform that gives developers access to hundreds of models through a single interface. The deal adds model selection and routing to Stripe's existing work around AI usage and token-based billing.

OpenRouter supports more than 400 models from over 80 providers, according to Stripe. Rather than requiring separate integrations with each model provider, developers can use OpenRouter to send requests through one API.

## Routing beyond model choice

The platform evaluates requests using factors including task complexity, price, speed, and reliability. It can then direct each request to a model suited to those requirements.

OpenRouter also handles a second layer of routing between providers serving the same model. Its documentation says customers can prioritise endpoints based on price, throughput, or latency, while setting requirements such as maximum prices or minimum performance levels.

The platform measures latency and throughput for individual model-provider combinations using rolling performance data. This allows a request to be routed to an endpoint that meets specified cost or performance criteria rather than relying on a fixed provider.

## Multi-model infrastructure expands

Multi-model environments are already common among surveyed organisations. F5's 2026 State of Application Strategy report found that 52% of organisations were chaining or orchestrating multiple AI models, with respondents using an average of seven models.

Menlo Ventures, an OpenRouter investor, reported that 66% of builders upgraded models while staying with their existing provider, while 11% switched vendors.

OpenRouter is also one of several infrastructure providers adding model routing. Snowflake announced dynamic model routing for Cortex AI Gateway on August 18.

AWS provides Intelligent Prompt Routing through Bedrock, while Microsoft Foundry offers routing profiles that balance model quality and price.

## Token usage meets billing

Stripe has also been developing token-based billing tools for AI applications. Its LLM token-billing service can meter consumption according to model and token type, including input, output, and cached tokens where supported.

Enterprise token consumption is already reaching large volumes. Deloitte surveyed 515 US-based business and technology decision-makers in late 2025. The survey found that 37% of respondents were consuming between one billion and 10 billion AI tokens per month, while another 30% were consuming more than 10 billion.

OpenRouter says it processes more than 10 trillion tokens per day across a community of more than 10 million developers and companies."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/amazons-prime-air-autonomous-drones-to-reach-500-us-cities/",
        "slug": "amazons-prime-air-autonomous-drones-to-reach-500-us-cities",
        "title": "Amazon's Prime Air autonomous drones to reach 500 US cities",
        "author": "Ryan Daws",
        "date": "August 20, 2026",
        "description": "Amazon plans to expand its Prime Air drone delivery service to nearly 500 cities and towns across the US by the end of 2026.",
        "image": "images/amazon-drones.jpg",
        "tags": ["amazon", "autonomous flight", "aviation", "computer vision", "drone delivery", "drones", "e-commerce", "edge computing", "logistics", "physical ai", "retail"],
        "categories": ["AI in Action", "Computer Vision", "Featured", "Physical AI", "Retail Logistics"],
        "body": """Amazon plans to expand its Prime Air drone delivery service to nearly 500 cities and towns across the US by the end of 2026. That build-out amounts to six times the number of locations Prime Air serves today, extending the option to communities with tens of millions of customers.

Reaching that many locations without adding pilots to each flight depends on the drones' own decision-making systems rather than a large ground staff monitoring individual flights. Prime Air's fleet runs on what Amazon calls "highly autonomous" flight software, engineered to keep functioning safely and predictably when something unexpected happens mid-flight.

A Detect-and-Avoid system sits at the centre of that setup, continuously scanning the airspace and surroundings around each drone much like a pilot checking for other aircraft. That scanning lets the drone spot obstacles on its own and make real-time flight decisions without a remote operator stepping in.

## FAA Part 135 certification supports the expansion

Prime Air operates under Federal Aviation Administration Part 135 certification, the licence category used for commercial air carriers. Amazon points to this as the highest tier of FAA oversight available to a drone delivery operation.

The safety systems extend to landing behaviour under adverse conditions. Amazon says its advanced safety systems are built to bring a drone to a safe landing in the event of severe weather or other unexpected events, with the stated goal of protecting people, pets, and property on the ground.

## Tiered logistics network built around speed

Prime Air carries items weighing five pounds or less that fit in a large shoebox, a limit Amazon says covers more than 60 percent of the items customers most frequently buy on the platform.

The eligible catalogue spans millions of items at Amazon's standard pricing, including groceries, cosmetics, medications, and electronics. Specific examples Amazon lists include iPhones, Samsung Galaxy handsets, Apple AirTags and AirPods, Ring doorbells.

Orders can land in as fast as 30 minutes, though Amazon puts the typical wait closer to 60 minutes after checkout. The fee structure ties to Prime status and order size.

## Current footprint and what comes next

11 Prime Air sites now cover 10 metro areas across seven states. Arizona's site sits in Tolleson, near Phoenix, and Florida's sits in Ruskin, near Tampa. Kansas City and Baton Rouge each host a single site. Michigan runs two in Hazel Park and Pontiac. Omaha's operation is in Papillion, Nebraska, and Texas alone accounts for four locations.

Amazon reports that Prime Air's drone delivery sites post the highest average delivery volumes of any US drone operation, with thousands of deliveries made daily.

David Carbon, VP of Amazon Prime Air, said: Customers already turn to Amazon for fast Same- and Next-Day Delivery, and Prime Air provides them an even speedier option when they need it, with deliveries in as fast as 30 minutes.

Amazon plans to launch Prime Air service soon in the Chicago, Syracuse, Cleveland, Atlanta, and Boise metro areas, with further communities scheduled to follow later this year."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/agentic-ai-in-government-uae-classification/",
        "slug": "agentic-ai-in-government-uae-classification",
        "title": "Agentic AI in government just hit the hard part: deciding what a machine may decide",
        "author": "Staff Writer",
        "date": "August 20, 2026",
        "description": "Agentic AI in government is moving beyond technical capability and into the domain of determining what decisions machines are allowed to make.",
        "image": "images/agentic-ai.jpg",
        "tags": ["agentic ai", "government", "regulation", "uae", "autonomous systems", "oversight"],
        "categories": ["AI in Action", "AI and Us"],
        "body": """Agentic AI in government just hit the hard part: deciding what a machine may decide.

The UAE government is among the first jurisdictions to formally classify and regulate agentic AI systems in public-sector operations. After deploying AI-assisted tools for document processing, permit routing, and service chatbots, policymakers are now grappling with which decisions can an autonomous agent make on its own, and which require human oversight.

This shift reflects a broader global trend. As agentic systems move from summarising documents to taking actions - booking appointments, initiating payments, allocating resources - the boundary between assistance and authority is blurring.

## Classification frameworks under development

The UAE's approach mirrors frameworks being discussed at the EU and US level. Agentic AI systems are being placed into tiers based on three criteria:

1. Autonomy level: How much human input does the system require to operate?
2. Impact scope: What is the potential harm if the system makes a wrong decision?
3. Intervention capability: Can a human override or reverse the system's actions in real-time?

Under the proposed system, Level 1 agents can suggest actions but must always defer to human approval. Level 2 agents can execute routine tasks within predefined parameters. Level 3 agents can make decisions in non-critical domains but must log all actions for audit.

## The accountability gap

"Once an agent can act without a human in the loop, we need to be able to answer the question: who is responsible when something goes wrong?" said a senior official familiar with the draft regulations.

The challenge is compounded by the fact that agentic systems often operate across multiple jurisdictions. An AI agent helping with visa processing in Dubai might pull data from federal databases, apply machine learning models hosted in another country.

## Real-world pilot programs

Several UAE government entities are already running pilot programs with agentic AI:

- Dubai Land Department: An agentic system that can verify property ownership, calculate transfer fees, and draft preliminary sale agreements.
- Ministry of Human Resources: An AI agent that assists with visa applications, checking eligibility, gathering required documents.
- Abu Dhabi Court of First Instance: A legal research agent that can access case law, summarize relevant precedents.

Each pilot operates under strict monitoring protocols, with every agent action logged and reviewed weekly by human supervisors.

## What comes next

Regulators expect the classification framework to be finalized by early 2027, with pilot programs continuing through the end of 2026. The EU is watching closely, as several member states are considering similar approaches."""
    }
]


# ============================================================================
# DESIGN SYSTEM (Swiss / Modernist — no slop)
# ============================================================================

FONTS = """
<link rel="preconnect" href="https://fonts.gstatic.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Crimson+Text:wght@300;400;600;700&display=swap" rel="stylesheet">
"""

CSS = """
/* AI News - Swiss/Modernist Design System */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Crimson+Text:wght@300;400;600;700&display=swap');

:root {
  --canvas: #000000;
  --surface: #070708;
  --border: #1a1a1c;
  --text: #e8e8ea;
  --text-dim: #a8a8b0;
  --text-dim2: #7a7a82;
  --accent: #8b5cf6;
  --accent-soft: #a897f7;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { font-size: 18px; scroll-behavior: smooth; }
body {
  background: var(--canvas);
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  line-height: 1.65;
  font-size: 18px;
  font-weight: 300;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-image:
    radial-gradient(circle at 10% 20%, rgba(139, 92, 246, 0.03) 0%, transparent 20%),
    radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.02) 0%, transparent 20%);
}

/* Typography hierarchy: serif headings, sans body */
h1, h2, h3, .h1, .h2, .h3 {
  font-family: 'Crimson Text', Georgia, 'Times New Roman', serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--text);
}
h1 { font-size: 3.2rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.4rem; }

/* Sans for UI elements */
nav, .meta, .category-tag, .tag, footer h4 {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Mono for metadata */
.byline, .date, .read-time, .tag-count {
  font-family: 'SFMono-Regular', 'Fira Code', 'Menlo', 'Monaco', monospace;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

a { color: var(--accent-soft); text-decoration: none; }
a:hover { opacity: 0.7; }
a.no-decorate:hover { opacity: 1; }

.container { max-width: 1100px; margin: 0 auto; padding: 0 32px; }
.wrapper { max-width: 820px; margin: 0 auto; }

/* ===== Header ===== */
header {
  background: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.88));
  backdrop-filter: blur(20px) saturate(200%);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 18px 0;
  transition: border-color 0.2s;
}
header.scrolled { border-bottom-color: var(--accent); }

header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-family: 'Inter', sans-serif;
  color: var(--text);
}
.logo .dot {
  width: 8px;
  height: 8px;
  background: var(--accent);
  border-radius: 50%;
  box-shadow: 0 0 20px var(--accent);
  flex-shrink: 0;
}

nav ul {
  display: flex;
  gap: 32px;
  list-style: none;
}
nav a {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
nav a:hover { color: var(--text); }
nav a.active { color: var(--text); border-bottom: 1px solid var(--accent); }

/* ===== Category tags ===== */
.category-tag {
  display: inline-block;
  background: var(--surface);
  color: var(--accent);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 4px;
  border: 1px solid var(--border);
  margin-right: 8px;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-family: 'Inter', sans-serif;
}

.featured-badge {
  display: inline-block;
  background: var(--accent);
  color: var(--canvas);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 16px;
  font-family: 'Inter', sans-serif;
}

/* ===== Hero / Featured ===== */
.hero {
  position: relative;
  margin: 32px 0 48px;
  border: 1px solid var(--border);
  border-radius: 0;
  overflow: hidden;
  background: var(--surface);
}

.hero-image {
  width: 100%;
  height: 520px;
  object-fit: cover;
  display: block;
  filter: brightness(0.85) contrast(1.05);
}

.hero-content {
  padding: 40px;
}

.hero h1 {
  font-size: 2.8rem;
  max-width: 80ch;
  margin-bottom: 20px;
}

.hero .meta {
  display: flex;
  align-items: center;
  gap: 20px;
  color: var(--text-dim);
  font-size: 0.9rem;
  margin-bottom: 24px;
}

.hero .meta span {
  display: flex;
  align-items: center;
  gap: 8px;
}

.hero p, .hero .excerpt {
  font-size: 1.125rem;
  color: var(--text-dim);
  max-width: 75ch;
  margin-bottom: 24px;
  font-weight: 300;
  line-height: 1.7;
}

.hero .read-more {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--accent);
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.04em;
}

/* ===== Article Grid ===== */
.article-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 32px;
  margin: 40px 0;
}

.article-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 0;
  overflow: hidden;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: border-color 0.2s;
}

.article-card:hover {
  border-color: var(--accent);
}

.article-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
  transition: opacity 0.2s;
}

.article-card:hover img {
  opacity: 0.9;
}

.card-content {
  padding: 24px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.card-content h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 16px;
  line-height: 1.3;
  flex-grow: 1;
  font-family: 'Crimson Text', Georgia, serif;
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--text-dim);
  margin-bottom: 16px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}

.read-more-small {
  color: var(--accent);
  font-family: 'Inter', sans-serif;
  font-size: 0.85rem;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.read-more-small::after {
  content: ">";
  font-size: 1.1em;
}

/* ===== Article Page ===== */
.article-page {
  max-width: 820px;
  margin: 0 auto;
  padding: 56px 32px;
}

.article-page .category-tag {
  margin-bottom: 16px;
}

.article-page h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  font-weight: 600;
}

.article-page .meta {
  display: flex;
  align-items: center;
  gap: 24px;
  color: var(--text-dim);
  font-size: 0.9rem;
  margin-bottom: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
}

.article-page .byline {
  display: flex;
  align-items: center;
  gap: 8px;
}

.article-page img {
  width: 100%;
  height: auto;
  display: block;
  margin: 32px 0;
  border: 1px solid var(--border);
  border-radius: 0;
}

/* Article body typography */
.article-body {
  font-family: 'Crimson Text', Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.8;
  color: var(--text);
}

.article-body p {
  margin: 24px 0;
  color: var(--text);
}

.article-body p.lead {
  font-size: 1.25rem;
  font-weight: 300;
  color: var(--text-dim);
  font-style: italic;
  border-left: 2px solid var(--accent);
  padding-left: 20px;
  margin: 32px 0;
}

.article-body h2 {
  font-family: 'Crimson Text', Georgia, serif;
  font-size: 1.8rem;
  font-weight: 600;
  margin: 48px 0 20px;
  color: var(--text);
  border-bottom: 1px solid var(--border);
  padding-bottom: 8px;
}

.article-body h3 {
  font-family: 'Crimson Text', Georgia, serif;
  font-size: 1.4rem;
  font-weight: 600;
  margin: 32px 0 16px;
  color: var(--text);
}

.article-body blockquote {
  border-left: 2px solid var(--accent);
  padding: 4px 24px;
  margin: 32px 0;
  font-style: italic;
  color: var(--text-dim);
  font-size: 1.05rem;
}

.article-body ul, .article-body ol {
  margin: 24px 0;
  padding-left: 32px;
}

.article-body li {
  margin: 8px 0;
  font-size: 1.125rem;
  line-height: 1.7;
}

.article-body a {
  border-bottom: 1px solid var(--accent);
  padding-bottom: 1px;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 40px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
}

.tags a {
  color: var(--text-dim2);
  font-size: 0.8rem;
  background: var(--surface);
  padding: 4px 12px;
  border-radius: 4px;
  border: 1px solid var(--border);
  font-family: 'Inter', sans-serif;
}

.tags a:hover {
  color: var(--accent);
  border-color: var(--accent);
}

/* ===== Section Headers ===== */
.section-title {
  font-size: 2rem;
  font-weight: 600;
  font-family: 'Crimson Text', Georgia, serif;
  margin: 0 0 24px;
  color: var(--text);
  border-bottom: 1px solid var(--border);
  padding-bottom: 12px;
  display: inline-block;
}

.category-section h3 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-dim);
  font-family: 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin: 32px 0 16px;
}

/* ===== Footer ===== */
footer {
  border-top: 1px solid var(--border);
  padding: 56px 0 32px;
  margin-top: 64px;
}

footer .top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}

footer .logo { font-size: 20px; }

footer .tagline {
  color: var(--text-dim);
  font-size: 14px;
  font-family: 'Inter', sans-serif;
}

footer .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 32px;
  margin-bottom: 32px;
}

footer h4 {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-dim);
  margin-bottom: 16px;
  font-family: 'Inter', sans-serif;
}

footer ul { list-style: none; }
footer li { margin-bottom: 10px; }
footer a {
  color: var(--text-dim);
  font-size: 15px;
  font-family: 'Inter', sans-serif;
}
footer a:hover { color: var(--accent); }

.copyright {
  text-align: center;
  color: var(--text-dim2);
  font-size: 0.85rem;
  padding-top: 32px;
  border-top: 1px solid var(--border);
  font-family: 'Inter', sans-serif;
}

/* ===== Subscribe ===== */
.subscribe-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 0;
  padding: 32px;
  margin: 40px 0;
}

.subscribe-box h3 {
  font-size: 1.25rem;
  margin-bottom: 16px;
  font-family: 'Crimson Text', Georgia, serif;
}

.subscribe-box p {
  color: var(--text-dim);
  margin-bottom: 20px;
  font-size: 1rem;
}

#subscribe-form {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

#subscribe-form input {
  flex: 1;
  min-width: 200px;
  padding: 12px 16px;
  border: 1px solid var(--border);
  background: var(--canvas);
  color: var(--text);
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  border-radius: 0;
}

#subscribe-form button {
  padding: 12px 24px;
  border: none;
  background: var(--accent);
  color: var(--canvas);
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  cursor: pointer;
  font-size: 15px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  border-radius: 0;
  transition: opacity 0.2s;
}

#subscribe-form button:hover {
  opacity: 0.8;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .container { padding: 0 20px; }
  nav ul { gap: 20px; }
  .hero h1 { font-size: 2.2rem; }
  .hero-image { height: 360px; }
  .hero-content { padding: 24px; }
  .article-grid { grid-template-columns: 1fr; }
  .article-page { padding: 40px 20px; }
  .article-page h1 { font-size: 2.2rem; }
  body { font-size: 17px; }
  .article-body { font-size: 1.05rem; }
  .article-body h2 { font-size: 1.6rem; }
  .section-title { font-size: 1.6rem; }
  #subscribe-form { flex-direction: column; }
  #subscribe-form input { min-width: auto; }
}
"""

JS = """// AI News - Swiss/Modernist site
document.addEventListener('DOMContentLoaded', function() {
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) { target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });

  // Scroll header effect
  const header = document.querySelector('header');
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 100) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // Lazy load images
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
    document.querySelectorAll('img[loading="lazy"]').forEach(img => imageObserver.observe(img));
  }
});
"""


def h(text):
    """HTML escape text."""
    return html.escape(str(text))


def render_cats(cats, max_count=3):
    if not cats:
        return ""
    return "".join(f'<span class="category-tag">{h(c)}</span>' for c in cats[:max_count])


def render_tags(tags):
    if not tags:
        return ""
    return "".join(f'<a href="#">{h(t)}</a>' for t in tags[:12])


def render_body(body_text):
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
                if item.strip() and item.strip().startswith("1."):
                    pass
                elif item.strip():
                    html_parts.append(f"<li>{h(item.strip().split('. ', 1)[-1] if '. ' in item else item.strip())}</li>")
            html_parts.append("</ol>")
        elif part.startswith("  - "):
            items = part.split("\n")
            html_parts.append("<ul>")
            for item in items:
                if item.strip():
                    html_parts.append(f"<li>{h(item.strip()[2:].strip())}</li>")
            html_parts.append("</ul>")
        else:
            cls = ' class="lead"' if i == 0 else ''
            text = h(part)
            # Preserve bold markers in body text
            text = text.replace("**", "<strong>").replace("<strong>", "<strong>", 1)
            html_parts.append(f"<p{cls}>{text}</p>")
    return "\n".join(html_parts)


def gen_homepage():
    featured = ARTICLES[0]
    latest = ARTICLES[:7]
    by_category = {}
    for a in ARTICLES[1:]:
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
  <title>AI News - Latest AI News, Insights, and Analysis</title>
  <meta name="description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide. No cookie walls, no paywalls.">
  <meta property="og:title" content="AI News - Latest AI News, Insights, and Analysis">
  <meta property="og:description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide.">
  <meta property="og:image" content="https://alkalinearchitect.github.io/ai-news-improved/{featured['image']}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="index,follow">
  {FONTS}
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
        {render_cats(featured.get('categories', []))}
        <h1>{h(featured['title'])}</h1>
        <div class="meta">
          <span class="byline">By {h(featured['author'])}</span>
          <span>&bull;</span>
          <span class="date">{h(featured['date'])}</span>
        </div>
        <p class="excerpt">{h(featured['description'])}</p>
        <a href="{featured['slug']}.html" class="read-more">Read full story</a>
      </div>
    </section>

    <section id="latest">
      <h2 class="section-title">Latest</h2>
      <div class="article-grid">
"""
    
    for article in latest[1:]:
        cats = render_cats(article.get("categories", []), 2)
        img = article.get("image", "")
        html += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{h(article['title'])}</h3>
            <div class="card-meta">
              <span class="date">{h(article['date'])}</span>
              <span class="byline">{h(article['author'])}</span>
            </div>
            <a href="{article['slug']}.html" class="read-more-small">Read &rarr;</a>
          </div>
        </article>
"""
    
    html += "\n      </div>\n    </section>\n"
    
    # Category sections
    html += '<section id="by-category">'
    html += '<h2 class="section-title">By Category</h2>'
    
    for cat, cat_articles in list(by_category.items())[:5]:
        html += f'<h3>{h(cat)}</h3>'
        html += '<div class="article-grid">'
        for article in cat_articles:
            cats = render_cats(article.get("categories", []), 1)
            img = article.get("image", "")
            html += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{h(article['title'])}</h3>
            <div class="card-meta">
              <span class="date">{h(article['date'])}</span>
            </div>
            <a href="{article['slug']}.html" class="read-more-small">Read &rarr;</a>
          </div>
        </article>
"""
        html += '</div>'
    
    html += '</section>'
    
    # Subscribe
    html += """
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
    html += """
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
    return html


def gen_article(article, all_articles):
    related = [a for a in all_articles if a["url"] != article["url"]][:4]
    cats = render_cats(article.get("categories", []))
    tags = render_tags(article.get("tags", []))
    body_html = render_body(article["body"])
    
    related_html = ""
    for rel in related:
        img = rel.get("image", "")
        rel_cats = render_cats(rel.get("categories", []), 1)
        related_html += f"""
        <article class="article-card">
          <img src="{img}" alt="{h(rel['title'])}" loading="lazy">
          <div class="card-content">
            {rel_cats}
            <h3>{h(rel['title'])}</h3>
            <div class="card-meta"><span class="date">{h(rel['date'])}</span></div>
            <a href="{rel['slug']}.html" class="read-more-small">Read &rarr;</a>
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
  <meta name="description" content="{h(article['description'][:160])}">
  <meta property="og:title" content="{h(article['title'])}">
  <meta property="og:description" content="{h(article['description'][:160])}">
  <meta property="og:image" content="https://alkalinearchitect.github.io/ai-news-improved/{article.get('image', '')}">
  <meta property="og:type" content="article">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="index,follow">
  {FONTS}
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
    
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(gen_homepage())
    
    for article in ARTICLES:
        with open(os.path.join(output_dir, f"{article['slug']}.html"), "w") as f:
            f.write(gen_article(article, ARTICLES))
    
    with open(os.path.join(output_dir, "data.json"), "w") as f:
        json.dump(ARTICLES, f, indent=2)
    
    print(f"Generated {len(ARTICLES) + 1} pages (1 homepage + {len(ARTICLES)} articles)")
    total_size = 0
    for f_name in sorted(os.listdir(output_dir)):
        f_path = os.path.join(output_dir, f_name)
        if os.path.isfile(f_path):
            size = os.path.getsize(f_path)
            total_size += size
            print(f"  {f_name} ({size:,} bytes)")
        elif os.path.isdir(f_path):
            print(f"  {f_name}/ ({len(os.listdir(f_path))} files)")
    print(f"  Total size: {total_size:,} bytes")


if __name__ == "__main__":
    print("=" * 60)
    print("AI News - World-Class Site Generator")
    print("Swiss/Modernist Design System")
    print("=" * 60)
    print()
    generate_site()
