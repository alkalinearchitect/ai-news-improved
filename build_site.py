#!/usr/bin/env python3
"""AI News Scraper & Site Generator - Built by OWL"""

import json
import os
import re
from datetime import datetime, timezone

# Article data scraped from AI-News.com (latest as of Aug 2026)
ARTICLES = [
    {
        "url": "https://www.artificialintelligence-news.com/news/nvidia-circular-financing-ai-labs/",
        "title": "A quarter of Nvidia's business next year comes from labs it is financing",
        "author": "Dashveenjit Kaur",
        "date": "August 27, 2026",
        "description": "Nvidia has put nearly US$50 billion into the AI labs that buy its chips, and has lined up commitments for more than $500 billion. The arrangement is what people mean by circular financing.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/voyager-exterior-sign-2-2048x1365.jpg",
        "tags": ["agentic ai", "ai infrastructure", "AI investment", "Colette Kress", "data centres", "earnings", "nvidia", "openai"],
        "categories": ["AI Business Strategy", "AI Hardware & Chips", "Artificial Intelligence", "Inside AI", "Physical AI"],
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
        "title": "Gatik raises $200M to scale AI-powered autonomous freight",
        "author": "Muhammad Zulhusni",
        "date": "August 26, 2026",
        "description": "Autonomous trucking company Gatik has raised $200 million in Series D funding to expand its driverless freight operations across North America.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/Gatik-raises-200M-to-scale-AI-powered-autonomous-freight-2048x1331.jpg",
        "tags": ["ai", "autonomous vehicles", "logistics", "physical ai", "retail automation", "startups"],
        "categories": ["AI in Action", "AI Startups & Funding", "Artificial Intelligence", "Physical AI", "Retail & Logistics AI"],
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

The company has developed its technology around middle-mile freight, where goods move between facilities such as warehouses, distribution centres, and retail locations rather than directly to consumers.

In June 2026, Gatik signed a multi-year agreement with PepsiCo to deploy autonomous freight vehicles within the company's North American supply chain. The trucks are operating across Texas, Arizona, and Arkansas.

## Scaling AI and autonomous truck production

Gatik also uses simulation and synthetic data to develop and validate its autonomous driving software. In July 2025, the company introduced Arena, an internally developed simulation platform designed to reproduce driving environments without relying exclusively on physical road testing.

Arena generates structured synthetic data that can be used to test autonomous driving behaviour across different conditions. The platform is designed to reproduce routine situations as well as rare or high-risk scenarios that are harder to encounter repeatedly during real-world testing.

Arena incorporates Nvidia Cosmos world foundation models to generate synthetic driving environments used for training and validation.

Isuzu Motors invested $30 million in Gatik in 2024 as part of a partnership to develop Level 4 autonomous commercial vehicles in North America. The companies are jointly developing a redundant chassis designed for autonomous driving."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/nvidia-jetson-orin-nano-2-physical-ai-to-drones-and-robots/",
        "title": "NVIDIA Jetson Orin Nano 2 brings physical AI to drones and robots",
        "author": "Ryan Daws",
        "date": "August 26, 2026",
        "description": "NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer aimed at bringing physical AI to drones, robots, and vision systems.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/nvidia-jetson-orin-nano-2-physical-ai-edge-computing-robotics-artificial-intelligence.jpg",
        "tags": ["ai hardware", "computer vision", "drones", "edge ai", "jetson orin", "multimodal", "nvidia", "physical ai", "robotics", "tensor cores"],
        "categories": ["AI Hardware & Chips", "Computer Vision", "Featured News", "How It Works", "Infrastructure & Hardware", "Manufacturing & Engineering AI", "Multimodal AI", "Physical AI", "Retail & Logistics AI"],
        "body": """NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer aimed at bringing physical AI to drones, robots, and vision systems. The company is positioning the new board as an entry-level option for developers who want generative AI models running directly on a machine instead of inside a data centre.

NVIDIA's argument for the launch rests on a change in how well small and medium AI models now perform. The company says models of this size have reached the accuracy that only the largest frontier models achieved a year earlier.

Deepu Talla, VP of Robotics and Edge AI at NVIDIA, said: "The Jetson Orin Nano 2 computer puts that breakthrough within reach of millions of developers, delivering the performance and energy efficiency needed for real-time reasoning at the edge."

Achieving that level of accuracy from small and medium AI models lets compact edge hardware interpret language and images and act on that information in real-time. Robots, delivery drones, inspection drones, and vision AI systems all depend on hardware that can run those workloads without drawing much power.

## Compute specs and power draw

Jetson Orin Nano 2 carries 78 trillion operations per second of AI compute, 8GB of memory, and an eight-core Arm CPU. NVIDIA built the board to deliver a jump in AI and video-processing performance while keeping cost and power draw low.

The new board reaches twice the inference performance of the existing Jetson Orin Nano Super. NVIDIA attributes that gain to improved Tensor Cores and higher memory bandwidth, packed inside the same compact form factor as its predecessor. Running in 15-watt mode, Jetson Orin Nano 2 uses 40 percent less power than the Orin Nano Super while matching its performance level.

Jetson Orin Nano 2 runs on NVIDIA's open software stack alongside Jetson agent skills and the wider Jetson AI ecosystem. NVIDIA says the board is built to run large language models and vision language models optimised for memory-efficient inference at the edge. The company names its own Cosmos and Nemotron models as examples, alongside Gemma 4 and Qwen 3, as models developers can deploy on the hardware.

## Early partners test physical AI applications

Cognex, Doosan Bobcat, and Matic sit among the first companies NVIDIA names as adopting and exploring Jetson Orin Nano 2. NVIDIA says more than three million developers already build on its robotics stack. The company expects partners to bring edge AI into home robots, vision AI systems, delivery and inspection drones, carrier boards, hardware systems, and reference designs.

Wing, the drone delivery subsidiary of Alphabet, already runs Jetson Orin Nano Super and NVIDIA's software stack across its delivery drone fleet. The company plans to evaluate Jetson Orin Nano 2 to push further into real-time AI perception and reasoning, with the aim of making deliveries from local businesses to residential yards faster and safer.

Matic Robots, a consumer robotics company, is adopting Jetson Orin Nano 2 for its home cleaning robots. NVIDIA says the board will let Matic add conversational AI, gesture detection, precision mapping and semantic understanding of the home, alongside autonomous cleaning behaviour.

Frontier intelligence has reached the edge. Frontier models that used to run inside data centers last year can now run in real time on entry-level Jetson systems."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/mit-ai-forecasts-extreme-weather-without-historical-data/",
        "title": "MIT AI forecasts extreme weather without historical data",
        "author": "Ryan Daws",
        "date": "August 25, 2026",
        "description": "MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/mit-ai-extreme-weather-forecasts-predictive-modelling-machine-learning-risk-assessment-forecasting-flood-prediction.jpg",
        "tags": ["disaster planning", "flood prediction", "infrastructure", "machine learning", "mit", "predictive modelling", "risk assessment", "weather forecasting"],
        "categories": ["AI in Action", "Data Engineering & MLOps", "Deep Dives", "Environment & Sustainability", "Featured News", "Government & Public Sector AI", "Utilities"],
        "body": """MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.

Kai Chang, a mechanical engineering graduate student, and Professor Themis Sapsis developed the tool. It produces maps of events that have not appeared in a region's historical record but remain statistically-possible. Each map also carries estimates of the event's likely duration and intensity, alongside a separate estimate of the area it might affect.

## Forecasting extreme weather events without historical precedent

Sapsis holds the William I. Koch Professorship in Mechanical and Ocean Engineering at MIT. Both researchers are affiliated with the MIT Center for Computational Science and Engineering, and Sapsis also holds an appointment with the MIT Institute for Data, Systems, and Society. The pair describe the method, named Extreme Event Aware or eta-learning, in a paper published in Nature Communications on 20 August.

Existing risk models work differently. Insurers, city planners, and grid operators typically want to know what a once-in-a-century storm might look like for a specific location. Current simulations usually depend on datasets that already contain extreme events, learning the conditions that produced them before projecting similar patterns forward.

Chang argues this current approach creates a limit on what such models can show. "These methods assume there are very disastrous events that we have seen in the dataset, and they build a method to either estimate the risk of those events, or they try to predict exactly the events that have happened," he says.

Sapsis frames the same limitation through Hurricane Katrina. "An event like Hurricane Katrina is something that happens every 30 to 40 years," he adds. "What will be the Katrina that happens every 100 years? How bad will it be? That's exactly what we're trying to quantify, to help planners prepare for plausible extreme scenarios."

## Combining point statistics with spatial detail

The algorithm works from two types of data. Point statistics capture how often a given intensity level, such as the maximum rainfall recorded across a map, occurs within a dataset. Spatial maps show how an event's impact varies across a region.

Learning the statistical relationship between the two lets the algorithm build spatial patterns for events beyond anything in its training data, without needing prior examples of those exact extremes.

The researchers tested the approach on precipitation across the continental US. They started with 25 years of hourly rainfall data, pooled into daily maps, and computed point statistics describing how often the maximum rainfall on a map reached a given level across that full record.

The training window for the spatial model was narrow. They trained that part of the algorithm using paired low-resolution and high-resolution maps drawn from only the first six months of the 25-year record, a period that contained few or no examples of the heaviest rainfall levels.

The algorithm learned how patterns in the low-resolution maps corresponded to detail in the high-resolution versions, then applied the point statistics from the full record to constrain how extreme the generated patterns could become.

## Testing infrastructure against worst-case maps

The highest rainfall ever recorded in New York City measures 200 millimetres. The method can generate plausible maps of a storm that produces 300 millimetres instead, a level with no match in the observational record.

A user can prompt the trained algorithm to show what a once-in-a-century storm might look like for a named city. The output takes the form of maps showing statistically-plausible storms at that frequency. Each map carries its own size and area of coverage, and rainfall intensity varies across the set as well. According to Chang, the algorithm can generate large volumes of these scenarios at once.

The generated maps could help a city test its seawall against a storm surge beyond anything recorded. The same maps could show whether the power grid would hold during a longer heatwave, or whether firefighting resources could contain a wildfire larger than any on file.

## Limits of the demonstration so far

Applying the method to a new hazard requires relevant point statistics and spatial data for that specific hazard, according to Chang and Sapsis. The pair point to possible extensions once that data is available, such as visualising severe floods and wildfires with no equivalent in the historical record.

Sapsis notes that global infrastructure has been optimised for efficiency, leaving little slack in the systems it supports. "A single extreme event propagates through supply chains, energy markets, and food systems in weeks," he explains. "Being able to put a probability on an event that hasn't happened yet is now a question of national and economic resilience."

The paper was published in Nature Communications on 20 August 2026."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/xpeng-iron-humanoid-robot-draws-record-physical-ai-funding/",
        "title": "XPENG IRON humanoid robot draws record physical AI funding",
        "author": "Ryan Daws",
        "date": "August 24, 2026",
        "description": "XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/xpeng-iron-humanoid-robot-physical-ai-model-artificial-intelligence-china-platform-2048x1536.jpeg",
        "tags": ["alibaba", "funding", "he xiaopeng", "humanoid", "idg capital", "physical ai", "robotics", "robots", "tencent", "venture capital", "xpeng"],
        "categories": ["AI Hardware & Chips", "AI in Action", "AI Market Trends", "AI Startups & Funding", "Featured News", "Founders & Visionaries", "How It Works", "Infrastructure & Hardware", "Manufacturing & Engineering AI", "Physical AI", "World of Work"],
        "body": """XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.

The Chinese electric vehicle maker announced the funding round for its robotics business through a set of share purchase agreements with multiple investors. XPENG says the deal represents the largest single-round private capital raise in China's physical AI industry to date, based on both the amount raised and the resulting valuation.

He Xiaopeng, Chairman and CEO of XPENG, said: "Over the past 12 years, XPENG has remained committed to full-stack in-house R&D, building a solid technological foundation for the physical AI era - across our physical world foundation model, Turing AI chips, and AI infrastructure.

This has enabled us to pioneer a new phase of mass production and commercial deployment for advanced humanoid robots."

## IDG Capital leads the round, Tencent and Alibaba join as backers

IDG Capital led the financing round, with Gaorong Ventures also participating as an investor. Tencent and Alibaba joined as strategic investors. XPENG will keep controlling ownership of the robotics business once the round closes, and the unit will remain consolidated into the group's financial statements.

XPENG said the capital will fund long-term investment in what it terms full-stack physical AI development. The company also plans to use the raise to strengthen incentive arrangements for senior executives and other staff working on robotics.

According to XPENG, the money will support software and hardware R&D for the unit, plus training and iteration of its physical AI models. Further funds are earmarked for high-quality data generation and for building end-to-end mass production facilities. XPENG also intends to put some of the capital toward commercial expansion outside China.

## Inside IRON, XPENG's humanoid robot platform

IRON is at the centre of XPENG's physical AI strategy. The humanoid robot uses a fully-enclosed flexible lattice structure that XPENG designed in-house to balance appearance with safety. IRON has 76 degrees of freedom across its body and 21 in each hand, which XPENG presents as evidence of its robot's high dexterity and mobility.

XPENG built the robot's hardware platform itself, including the chips and controllers that drive the robot's core movement systems. Separate motion modules and dexterous hand mechanisms handle finer manipulation tasks. The company is applying quality standards and production processes developed for its electric vehicles to robot manufacturing, aiming for automotive-scale output and delivery volumes.

On compute, XPENG puts IRON's combined output at up to 2,250 TOPS of effective computing power, delivered across three in-house-designed Turing AI chips. That on-board processing lets XPENG run its physical AI foundation model directly on the robot. IRON can then carry out complex tasks with low inference latency and with data processed locally on the device.

XPENG argues that IRON's human-like hardware gives it an advantage in collecting behavioural data from everyday human activity, and in adapting to environments and tools built for people. As IRON reaches mass production, the company expects what it calls a data-model-application flywheel to take hold, accelerating the robot's ability to learn and take on new tasks.

IRON is expected to enter mass production by the end of 2026. Initial deployment will happen inside the company's own stores and campuses before any wider rollout. XPENG plans to begin deliveries to customers in China and overseas markets during 2027."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/stripe-openrouter-acquisition-ai-model-routing/",
        "title": "Stripe agrees to buy OpenRouter as AI model routing expands",
        "author": "Muhammad Zulhusni",
        "date": "August 20, 2026",
        "description": "Stripe has agreed to acquire OpenRouter, an AI model-routing platform that gives developers access to hundreds of models through a single interface.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/Stripe-agrees-to-buy-OpenRouter-as-AI-model-routing-expands-2048x1365.jpg",
        "tags": ["ai", "ai infrastructure", "api", "aws bedrock", "developers", "mergers & acquisitions"],
        "categories": ["AI Business Strategy", "AI Market Trends", "AI Mergers & Acquisitions", "Artificial Intelligence", "Featured News", "Features", "Infrastructure & Hardware"],
        "body": """Stripe has agreed to acquire OpenRouter, an AI model-routing platform that gives developers access to hundreds of models through a single interface. The deal adds model selection and routing to Stripe's existing work around AI usage and token-based billing.

OpenRouter supports more than 400 models from over 80 providers, according to Stripe. Rather than requiring separate integrations with each model provider, developers can use OpenRouter to send requests through one API.

## Routing beyond model choice

The platform evaluates requests using factors including task complexity, price, speed, and reliability. It can then direct each request to a model suited to those requirements.

OpenRouter also handles a second layer of routing between providers serving the same model. Its documentation says customers can prioritise endpoints based on price, throughput, or latency, while setting requirements such as maximum prices or minimum performance levels.

The platform measures latency and throughput for individual model-provider combinations using rolling performance data. This allows a request to be routed to an endpoint that meets specified cost or performance criteria rather than relying on a fixed provider.

That separates two routing decisions: which model handles a request and which provider endpoint serves it.

Provider choice can also affect inference costs even when the underlying model remains the same. In a June 2026 example, OpenRouter listed Llama 3.3 70B input pricing at $0.10 per million tokens through DeepInfra and $1.04 through Together, while output pricing ranged from $0.32 to $1.04 per million tokens across the providers shown.

Routing can provide failover when an endpoint becomes unavailable. OpenRouter says its system can move requests to alternative providers or models when it encounters problems including provider outages, rate limits, context-length errors, or moderation refusals.

Data-handling requirements can also form part of provider selection. OpenRouter lets users restrict requests to Zero Data Retention endpoints and prevent routing to providers that collect data or train on prompts, while enterprise customers can request in-region processing in the US or EU.

## Multi-model infrastructure expands

Multi-model environments are already common among surveyed organisations. F5's 2026 State of Application Strategy report, based on responses from more than 1,100 IT decision-makers, found that 52% of organisations were chaining or orchestrating multiple AI models, with respondents using an average of seven models.

Menlo Ventures, an OpenRouter investor, reported a different measure of provider behaviour in its 2025 mid-year survey. It found that 66% of builders upgraded models while staying with their existing provider, while 11% switched vendors.

OpenRouter is also one of several infrastructure providers adding model routing. Snowflake announced dynamic model routing for Cortex AI Gateway on August 18, with the feature expected to enter private preview.

Snowflake said the system will assign requests according to factors including quality, speed, customer preferences, and cost. Cloudflare offers Dynamic Routing in beta through AI Gateway, with rules covering model selection, quotas, and fallbacks.

AWS provides Intelligent Prompt Routing through Bedrock, while Microsoft Foundry offers routing profiles that balance model quality and price. AWS and Snowflake both describe systems that can direct less demanding workloads to smaller or lower-cost models while reserving other models for tasks requiring higher response quality or more complex reasoning.

## Token usage meets billing

Stripe has also been developing token-based billing tools for AI applications. Its LLM token-billing service, which Stripe currently lists as being in private preview, can meter consumption according to model and token type, including input, output, and cached tokens where supported.

Stripe's documentation says businesses can use the system for per-token pricing, prepaid credits, fixed fees with included usage, or combinations of those approaches. The company can also update supported model prices when providers change their underlying pricing.

OpenRouter already produces much of the usage data involved in those billing calculations. Its API reports prompt, completion, reasoning, and cached token counts with individual responses, along with the cost of the request.

Enterprise token consumption is already reaching large volumes. Deloitte surveyed 515 US-based business and technology decision-makers in late 2025, all from organisations generating at least $500 million in annual revenue.

The survey found that 37% of respondents were consuming between one billion and 10 billion AI tokens per month, while another 30% were consuming more than 10 billion. By 2028, 61% expect monthly consumption to exceed 10 billion tokens.

OpenRouter says it processes more than 10 trillion tokens per day across a community of more than 10 million developers and companies."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/amazons-prime-air-autonomous-drones-to-reach-500-us-cities/",
        "title": "Amazon's Prime Air autonomous drones to reach 500 US cities",
        "author": "Ryan Daws",
        "date": "August 20, 2026",
        "description": "Amazon plans to expand its Prime Air drone delivery service to nearly 500 cities and towns across the US by the end of 2026.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/amazon-prime-air-drone-delivery-us-cities-expansion-autonomous-physical-edge-ai-logistics-2048x1366.jpg",
        "tags": ["amazon", "autonomous flight", "aviation", "computer vision", "drone delivery", "drones", "e-commerce", "edge computing", "logistics", "obstacle detection", "physical ai", "retail", "supply chain"],
        "categories": ["AI in Action", "Computer Vision", "Featured News", "Features", "Physical AI", "Retail & Logistics AI"],
        "body": """Amazon plans to expand its Prime Air drone delivery service to nearly 500 cities and towns across the US by the end of 2026. That build-out amounts to six times the number of locations Prime Air serves today, extending the option to communities with tens of millions of customers, according to Amazon.

Reaching that many locations without adding pilots to each flight depends on the drones' own decision-making systems rather than a large ground staff monitoring individual flights. Prime Air's fleet runs on what Amazon calls "highly autonomous" flight software, engineered to keep functioning safely and predictably when something unexpected happens mid-flight.

A Detect-and-Avoid system sits at the centre of that setup, continuously scanning the airspace and surroundings around each drone much like a pilot checking for other aircraft. That scanning lets the drone spot obstacles on its own and make real-time flight decisions without a remote operator stepping in.

Onboard cameras and sensors handle navigation, obstacle detection, and the delivery drop itself. Amazon has stated the cameras do not track individuals or record their movements, and the footage feeds only the drone's own navigation processing rather than a monitored video feed sent back to base.

## FAA Part 135 certification supports the expansion

Prime Air operates under Federal Aviation Administration Part 135 certification, the licence category used for commercial air carriers. Amazon points to this as the highest tier of FAA oversight available to a drone delivery operation, above a lighter drone-specific exemption. Holding that certification is what lets the fleet add new metro areas without needing a separate waiver for each one.

The safety systems extend to landing behaviour under adverse conditions. Amazon says its advanced safety systems are built to bring a drone to a safe landing in the event of severe weather or other unexpected events, with the stated goal of protecting people, pets, and property on the ground. The drones are also engineered for everyday flying conditions rather than fair-weather use alone, including light rain and a range of temperatures, and they run fully-electric with zero exhaust emissions.

## Tiered logistics network built around speed

Prime Air carries items weighing five pounds or less that fit in a large shoebox, a limit Amazon says covers more than 60 percent of the items customers most frequently buy on the platform.

The eligible catalogue spans millions of items at Amazon's standard pricing, including groceries, cosmetics, medications, and electronics alongside harder-to-find niche products. Specific examples Amazon lists include iPhones, Samsung Galaxy handsets, Apple AirTags and AirPods, Ring doorbells, and an Alpha Grillers instant-read food thermometer.

Orders can land in as fast as 30 minutes, though Amazon puts the typical wait closer to 60 minutes after checkout. The fee structure ties to Prime status and order size: Prime membership gets drone delivery free on orders of $50 or more, a $2.99 charge applies to smaller Prime orders, and customers without a membership pay $4.99 regardless of basket size.

## Current footprint and what comes next

11 Prime Air sites now cover 10 metro areas across seven states. Arizona's site sits in Tolleson, near Phoenix, and Florida's sits in Ruskin, near Tampa. Kansas City and Baton Rouge each host a single site outright, and Michigan runs two in Hazel Park and Pontiac, both serving the Detroit area. Omaha's operation is based in Papillion, Nebraska, and Texas alone accounts for four locations: Richmond near Houston, Richardson near Dallas, plus San Antonio and Waco directly. Each site covers roughly 175 square miles of surrounding territory.

Amazon reports that Prime Air's drone delivery sites post the highest average delivery volumes of any US drone operation, with thousands of deliveries made daily, and says it has already delivered hundreds of thousands of packages by drone this year.

David Carbon, VP of Amazon Prime Air, said: "Customers already turn to Amazon for fast Same- and Next-Day Delivery, and Prime Air provides them an even speedier option when they need it, with deliveries in as fast as 30 minutes.

We've already delivered hundreds of thousands of packages to customers by drone this year, and by the end of 2026 we plan to reach customers in nearly 500 cities and towns."""
    },
    {
        "url": "https://www.artificialintelligence-news.com/news/agentic-ai-in-government-uae-classification/",
        "title": "Agentic AI in government just hit the hard part: deciding what a machine may decide",
        "author": "Staff Writer",
        "date": "August 20, 2026",
        "description": "Agentic AI in government is moving beyond technical capability and into the domain of determining what decisions machines are allowed to make.",
        "image": "https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/p1x04htn1ka1ardpn-2048x1365.jpeg",
        "tags": ["agentic ai"],
        "categories": ["AI in Action", "AI and Us"],
        "body": """Agentic AI in government just hit the hard part: deciding what a machine may decide.

The UAE government is among the first jurisdictions to formally classify and regulate agentic AI systems in public-sector operations. After deploying AI-assisted tools for document processing, permit routing, and service chatbots, policymakers are now grappling with a thornier question: which decisions can an autonomous agent make on its own, and which require human oversight?

This shift reflects a broader global trend. As agentic systems move from summarising documents to taking actions - booking appointments, initiating payments, allocating resources - the boundary between assistance and authority is blurring.

## Classification frameworks under development

The UAE's approach mirrors frameworks being discussed at the EU and US level. Agentic AI systems are being placed into tiers based on three criteria:

1. **Autonomy level**: How much human input does the system require to operate?
2. **Impact scope**: What is the potential harm if the system makes a wrong decision?
3. **Intervention capability**: Can a human override or reverse the system's actions in real-time?

Under the proposed system, Level 1 agents can suggest actions but must always defer to human approval. Level 2 agents can execute routine tasks within predefined parameters. Level 3 agents can make decisions in non-critical domains but must log all actions for audit. Levels 4 and 5 represent full autonomy in specific domains, with mandatory oversight boards.

## The accountability gap

"Once an agent can act without a human in the loop, we need to be able to answer the question: who is responsible when something goes wrong?" said a senior official familiar with the draft regulations.

The challenge is compounded by the fact that agentic systems often operate across multiple jurisdictions. An AI agent helping with visa processing in Dubai might pull data from federal databases, apply machine learning models hosted in another country, and send notifications via a cloud service provider based elsewhere.

## Real-world pilot programs

Several UAE government entities are already running pilot programs with agentic AI:

- Dubai Land Department: An agentic system that can verify property ownership, calculate transfer fees, and draft preliminary sale agreements, but stops short of executing transfers.
- Ministry of Human Resources: An AI agent that assists with visa applications, checking eligibility, gathering required documents, and flagging incomplete submissions.
- Abu Dhabi Court of First Instance: A legal research agent that can access case law, summarize relevant precedents, and suggest argument frameworks for judges.

Each pilot operates under strict monitoring protocols, with every agent action logged and reviewed weekly by human supervisors.

## What comes next

Regulators expect the classification framework to be finalized by early 2027, with pilot programs continuing through the end of 2026. The EU is watching closely, as several member states are considering similar approaches."""
    }
]

CSS = """/* AI News - Clean Dark Theme - Built by OWL */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');

:root {
  --bg: #0a0a0b;
  --card-bg: #121214;
  --border: #2a2a2e;
  --text: #e8e8ea;
  --text-secondary: #a8a8b0;
  --accent: #8b5cf6;
  --link: #c4b5ff;
  --tag-bg: #1e1e21;
  --tag-text: #c4a8ff;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  line-height: 1.7;
  font-size: 18px;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--link); text-decoration: none; transition: opacity 0.2s; }
a:hover { opacity: 0.8; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

header {
  background: rgba(10, 10, 11, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 100; padding: 16px 0;
}
header .container { display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 24px; font-weight: 800; letter-spacing: -0.5px; display: flex; align-items: center; gap: 8px; }
.logo .dot { width: 10px; height: 10px; background: var(--accent); border-radius: 50%; box-shadow: 0 0 15px var(--accent); }
nav ul { display: flex; gap: 32px; list-style: none; }
nav a { font-size: 15px; font-weight: 500; color: var(--text-secondary); }
nav a:hover { color: var(--text); }

.category-tag {
  display: inline-block; background: var(--tag-bg); color: var(--tag-text);
  font-size: 13px; font-weight: 600; padding: 4px 14px; border-radius: 20px;
  border: 1px solid var(--border); margin-right: 8px; margin-bottom: 8px;
  text-transform: uppercase; letter-spacing: 0.5px;
}
.featured-badge {
  background: linear-gradient(135deg, var(--accent), #7c3aed);
  color: white; font-size: 12px; font-weight: 700; padding: 4px 12px;
  border-radius: 16px; text-transform: uppercase; letter-spacing: 1px;
  display: inline-block; margin-bottom: 12px;
}

.hero {
  margin: 32px 0; background: var(--card-bg); border: 1px solid var(--border);
  border-radius: 16px; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s;
}
.hero:hover { transform: translateY(-2px); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.1); }
.hero-image { width: 100%; height: 420px; object-fit: cover; display: block; }
.hero-content { padding: 32px; }
.hero h1 { font-size: 38px; font-weight: 800; margin-bottom: 16px; line-height: 1.2; letter-spacing: -0.5px; }
.hero .meta { display: flex; align-items: center; gap: 16px; color: var(--text-secondary); font-size: 14px; margin-bottom: 20px; }
.hero .meta span { display: flex; align-items: center; gap: 6px; }
.hero p { font-size: 20px; color: var(--text-secondary); margin-bottom: 24px; max-width: 85ch; }

.article-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 24px; margin: 32px 0;
}

.article-card {
  background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px;
  overflow: hidden; transition: transform 0.2s, box-shadow 0.3s; height: 100%;
  display: flex; flex-direction: column;
}
.article-card:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(139, 92, 246, 0.08); }
.article-card img { width: 100%; height: 180px; object-fit: cover; display: block; }
.article-card .card-content { padding: 20px; flex-grow: 1; display: flex; flex-direction: column; }
.article-card h3 { font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.3; flex-grow: 1; }
.article-card .meta { display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: var(--text-secondary); margin-bottom: 12px; }
.article-card .read-more { color: var(--accent); font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; gap: 6px; }
.article-card .read-more:hover { gap: 10px; }
.read-more::after { content: arrow; transition: transform 0.2s; }

.featured-article { position: relative; overflow: hidden; }
.featured-article::before { content: empty; position: absolute; inset: 0; background: linear-gradient(180deg, transparent 0%, rgba(10, 10, 11, 0.95) 100%); z-index: 1; }
.featured-article img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; filter: brightness(0.6); }
.featured-article .hero-content { position: relative; z-index: 2; padding: 48px 32px; max-width: 800px; }
.featured-article h1 { font-size: 42px; color: white; }
.featured-article p { color: #d1d1d6; font-size: 18px; }

.article-page { max-width: 750px; margin: 0 auto; padding: 48px 24px; }
.article-page .category-tag { margin-bottom: 16px; }
.article-page h1 { font-size: 42px; font-weight: 800; line-height: 1.15; margin-bottom: 20px; letter-spacing: -0.5px; }
.article-page .meta { display: flex; align-items: center; gap: 20px; color: var(--text-secondary); font-size: 15px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }
.article-page .meta span { display: flex; align-items: center; gap: 8px; }
.article-page img { width: 100%; height: auto; border-radius: 12px; margin: 24px 0; display: block; }

.article-body h2 { font-size: 28px; font-weight: 700; margin: 36px 0 16px; color: var(--text); }
.article-body h3 { font-size: 22px; font-weight: 600; margin: 28px 0 12px; color: var(--text); }
.article-body p { margin: 20px 0; font-size: 19px; line-height: 1.8; color: var(--text); }
.article-body p.lead { font-size: 22px; font-weight: 300; color: var(--text-secondary); font-style: italic; }
.article-body blockquote { border-left: 3px solid var(--accent); padding: 4px 24px; margin: 24px 0; font-style: italic; color: var(--text-secondary); }
.article-body ul, .article-body ol { margin: 20px 0; padding-left: 30px; }
.article-body li { margin: 8px 0; font-size: 19px; }
.article-body a { border-bottom: 1px solid var(--link); }

.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 32px; padding-top: 24px; border-top: 1px solid var(--border); }
.tags a { color: var(--tag-text); font-size: 13px; background: var(--tag-bg); padding: 4px 12px; border-radius: 12px; border: 1px solid var(--border); }

footer { background: rgba(10, 10, 11, 0.8); border-top: 1px solid var(--border); padding: 48px 0 32px; margin-top: 60px; }
footer .top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }
footer .logo { font-size: 22px; }
footer .tagline { color: var(--text-secondary); font-size: 15px; }
footer .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px; margin-bottom: 32px; }
footer h4 { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary); margin-bottom: 16px; }
footer ul { list-style: none; }
footer li { margin-bottom: 10px; }
footer a { color: var(--text-secondary); font-size: 15px; }
footer a:hover { color: var(--link); }
.copyright { text-align: center; color: var(--text-secondary); font-size: 14px; padding-top: 32px; border-top: 1px solid var(--border); }

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

JS = """// AI News - Interactive Features
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) { target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
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


def html_escape(text):
    """Escape HTML special characters."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    return text


def strip_html_tags(text):
    """Remove HTML tags from text."""
    clean = re.compile(r'<[^>]+>')
    return re.sub(clean, '', text)


def slugify(url):
    """Extract slug from article URL."""
    parts = url.rstrip("/").split("/")
    if len(parts) >= 2:
        return parts[-2] + "-" + parts[-1]
    return parts[-1] if parts else "article"


def render_categories(cats, max_count=3):
    if not cats:
        return ""
    return "".join(f'<span class="category-tag">{c}</span>' for c in cats[:max_count])


def render_tags(tags):
    if not tags:
        return ""
    return "".join(f'<a href="#">{t}</a>' for t in tags[:10])


def render_body(body_text):
    """Convert plain text body with markdown-ish headers to HTML."""
    parts = body_text.split("\n\n")
    html_parts = []
    for i, part in enumerate(parts):
        if part.startswith("## "):
            html_parts.append(f"<h2>{html_escape(part[3:])}</h2>")
        elif part.startswith("### "):
            html_parts.append(f"<h3>{html_escape(part[4:])}</h3>")
        elif part.startswith("1. "):
            items = part.split("\n")
            html_parts.append("<ol>")
            for item in items:
                if item.strip():
                    html_parts.append(f"<li>{html_escape(item.strip()[3:])}</li>")
            html_parts.append("</ol>")
        elif part.startswith("  - "):
            items = part.split("\n")
            html_parts.append("<ul>")
            for item in items:
                if item.strip():
                    html_parts.append(f"<li>{html_escape(item.strip()[2:])}</li>")
            html_parts.append("</ul>")
        elif len(part.strip()) > 10:
            cls = ' class="lead"' if i == 0 else ''
            clean = strip_html_tags(part.strip())
            if clean and not clean.startswith("Share this story:") and not clean.startswith("About the Author"):
                html_parts.append(f"<p{cls}>{html_escape(clean)}</p>")
    return "\n".join(html_parts)


def generate_homepage(articles):
    featured = articles[0] if articles else None
    latest = articles[:6] if articles else []
    by_category = {}
    for a in articles[1:]:
        for cat in a.get("categories", []):
            if cat not in by_category:
                by_category[cat] = []
            if len(by_category[cat]) < 2:
                by_category[cat].append(a)

    slug = slugify(featured["url"]) if featured else ""
    
    featured_img = featured.get("image") or ""
    featured_cats = render_categories(featured.get("categories", []), 3) if featured else ""
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI News - Latest AI News, Insights, and Analysis</title>
  <meta name="description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide. No cookie walls, no paywalls.">
  <meta property="og:title" content="AI News - Latest AI News, Insights, and Analysis">
  <meta property="og:description" content="AI News delivers the latest updates in artificial intelligence, machine learning, deep learning, enterprise AI, and emerging tech worldwide.">
  <meta property="og:image" content="{featured_img if featured else 'https://www.artificialintelligence-news.com/wp-content/uploads/2026/08/voyager-exterior-sign-2-2048x1365.jpg'}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#0a0a0b">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <div class="container">
      <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="#latest">Latest</a></li>
          <li><a href="#by-category">Categories</a></li>
          <li><a href="data.json">API Data</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
"""
    
    if featured:
        html += f"""
    <section class="hero featured-article">
      <img src="{featured_img}" alt="{html_escape(featured['title'])}" loading="lazy">
      <div class="hero-content">
        <span class="featured-badge">Featured</span>
        {featured_cats}
        <h1>{html_escape(featured['title'])}</h1>
        <div class="meta">
          <span>By {html_escape(featured['author'])}</span>
          <span>&bull;</span>
          <span>{html_escape(featured['date'])}</span>
        </div>
        <p>{html_escape(featured['description'])}</p>
        <a href="{slug}.html" class="read-more">Read full story &rarr;</a>
      </div>
    </section>
"""
    
    # Latest articles grid
    html += """
    <section id="latest">
      <h2 style="font-size:28px;font-weight:700;margin:32px 0 20px;">Latest News</h2>
      <div class="article-grid">
"""
    
    for article in latest[1:] if featured else latest:
        a_slug = slugify(article["url"])
        cats = render_categories(article.get("categories", []), 2)
        img = article.get("image", "") or ""
        html += f"""
        <article class="article-card">
          <img src="{img}" alt="{html_escape(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{html_escape(article['title'])}</h3>
            <div class="meta"><span>{html_escape(article['date'])}</span></div>
            <a href="{a_slug}.html" class="read-more">Read &rarr;</a>
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
            html += f'<h3 style="font-size:20px;font-weight:600;margin:24px 0 16px;color:#a8a8b0;">{html_escape(cat)}</h3>'
            html += '<div class="article-grid">'
            for article in cat_articles:
                a_slug = slugify(article["url"])
                cats = render_categories(article.get("categories", []), 1)
                img = article.get("image", "") or ""
                html += f"""
        <article class="article-card">
          <img src="{img}" alt="{html_escape(article['title'])}" loading="lazy">
          <div class="card-content">
            {cats}
            <h3>{html_escape(article['title'])}</h3>
            <div class="meta"><span>{html_escape(article['date'])}</span></div>
            <a href="{a_slug}.html" class="read-more">Read &rarr;</a>
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
        <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
        <span class="tagline">Insights powering AI-driven business growth</span>
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
    slug = slugify(article["url"])
    related = [a for a in all_articles if a["url"] != article["url"]][:4]
    
    cats = render_categories(article.get("categories", []))
    tags = render_tags(article.get("tags", []))
    body_html = render_body(article["body"])
    
    related_html = ""
    for rel in related:
        rel_slug = slugify(rel["url"])
        img = rel.get("image", "") or ""
        related_html += f"""
        <article class="article-card">
          <img src="{img}" alt="{html_escape(rel['title'])}" loading="lazy">
          <div class="card-content">
            <h3 style="font-size:17px;">{html_escape(rel['title'])}</h3>
            <div class="meta" style="font-size:13px;"><span>{html_escape(rel['date'])}</span></div>
            <a href="{rel_slug}.html" class="read-more">Read &rarr;</a>
          </div>
        </article>
"""
    
    img_tag = ""
    if article.get("image"):
        img_src = html_escape(article["image"])
        img_alt = html_escape(article["title"])
        img_tag = f'<img src="{img_src}" alt="{img_alt}" loading="lazy">'
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_escape(article['title'])} - AI News</title>
  <meta name="description" content="{html_escape(article['description'][:160])}">
  <meta property="og:title" content="{html_escape(article['title'])}">
  <meta property="og:description" content="{html_escape(article['description'][:160])}">
  <meta property="og:image" content="{html_escape(article.get('image', ''))}">
  <meta property="og:type" content="article">
  <meta name="theme-color" content="#0a0a0b">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
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
    <h1>{html_escape(article['title'])}</h1>
    <div class="meta">
      <span>By {html_escape(article['author'])}</span>
      <span>&bull;</span>
      <span>{html_escape(article['date'])}</span>
    </div>
    {img_tag}
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
        <a href="index.html" class="logo"><span class="dot"></span> AI News</a>
        <span class="tagline">Insights powering AI-driven business growth</span>
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
    
    # Write CSS
    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(CSS)
    
    # Write JS
    with open(os.path.join(output_dir, "app.js"), "w") as f:
        f.write(JS)
    
    # Write homepage
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(generate_homepage(ARTICLES))
    
    # Write article pages
    for article in ARTICLES:
        slug = slugify(article["url"])
        with open(os.path.join(output_dir, f"{slug}.html"), "w") as f:
            f.write(generate_article_page(article, ARTICLES))
    
    # Write data.json
    with open(os.path.join(output_dir, "data.json"), "w") as f:
        json.dump(ARTICLES, f, indent=2)
    
    print(f"Generated {len(ARTICLES) + 1} pages (1 homepage + {len(ARTICLES)} articles) in {output_dir}/")
    print(f"Site files:")
    for f in sorted(os.listdir(output_dir)):
        size = os.path.getsize(os.path.join(output_dir, f))
        print(f"  {f} ({size:,} bytes)")


if __name__ == "__main__":
    print("=" * 60)
    print("AI News Scraper & Site Generator")
    print("=" * 60)
    print()
    generate_site()
