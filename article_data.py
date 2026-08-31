#!/usr/bin/env python3
"""
Article body content for AI News site.
Each article body uses ## for h2, ### for h3, 1. for ordered lists, - for bullets.
ASCII-safe only.
"""

ARTICLE_BODIES = {}

ARTICLE_BODIES["nvidia-circular-financing-ai-labs"] = """Nvidia has put nearly US$50 billion into the AI labs that buy its chips, and has lined up commitments for more than $500 billion in circular financing.

Colette Kress, the company's chief financial officer, told analysts on August 26 that demand from the labs Nvidia backs with its own balance sheet will contribute toward roughly a quarter of its business next year.

That arrangement is what people mean by circular financing, and Nvidia used the phrase before any analyst did. Kress said on the earnings call that the company recognised the scale of the support it was providing and knew some would call it circular financing. She said Nvidia sees it differently.

The loop is simple to describe. Nvidia invests in an AI lab. The lab uses the money, or the credit Nvidia's involvement unlocks, to build a data centre. The data centre is filled with Nvidia chips. The purchase is recorded as Nvidia revenue. Nvidia's share price and cash pile grow, and it invests again.

## What Nvidia has committed

Kress gave the figures herself. She said Nvidia has signed partnerships with six investment firms, naming Apollo Global Management, BlackRock, Blackstone, Brookfield Asset Management, Goldman Sachs and KKR, to set up financing platforms that will raise more than $500 billion of outside capital for the labs to build with.

She said Nvidia secured land, power and building capacity with SB Energy that will host only Nvidia equipment. The first phase supports 4.25 gigawatts and will be used by OpenAI. Kress put OpenAI's existing and planned commitments at around 12 gigawatts of Nvidia compute through 2030.

Nvidia's results statement describes those partnerships as subject to definitive agreements, which means the binding contracts have not been signed. The $500 billion is an intention rather than money in place.

## Why Nvidia rejects the circular financing label

Kress gave three answers, and they deserve to be reported alongside the numbers.

Outside lenders still assess every deal on its own merits, she said, and Nvidia is not making loans. The chips Nvidia ships go to customers that are investment grade or backed by someone who is. And if a customer does fail, the equipment can be moved to another buyer, which she offered as the reason Nvidia's exposure is limited.

Kress also explained why the labs need the help. They have more demand for computing than their finances can support, she said. They are young companies without the long contracts and credit ratings that lenders normally require before funding a data centre. What limits their growth is not customers or technology. It is access to computing.

The obvious risk is what happens if one of them cannot pay. Nvidia would lose the sale and the investment at the same time. Kress answers that the hardware finds another buyer. That claim only holds while demand exceeds supply, and Nvidia says it currently does.

## The agent assumption underneath it all

Kress told Morgan Stanley's Joseph Moore that an agent needs somewhere between 15 and 100 times the computing power of a person using the same system. Huang said he believes AI tipped over to being mostly agentic in the past month. On that basis, the company guided to $108 billion in revenue this quarter and said it preliminarily expects around 70% growth in the year to January 2028."""

ARTICLE_BODIES["gatik-200m-ai-autonomous-freight"] = """Autonomous trucking company Gatik has raised $200 million in Series D funding to expand its driverless freight operations across North America. The round was led by Qatar Investment Authority and Koch Disruptive Technologies.

Gatik said it has more than $600 million in contracted revenue and has completed 85,000 fully driverless orders. The company reported a 99% on-time delivery rate across its operations.

Its trucks currently move goods between distribution centres and stores across regional networks in Texas, Arizona, Arkansas, and Canada. Gatik operates dozens of fully driverless trucks and says it plans to expand the fleet to thousands over the coming years.

A Gatik spokesperson told Reuters that the company is targeting more than 100 driverless trucks by the end of 2026. Gatik plans to use the new capital to expand commercial operations and its fleet while continuing to invest in technology, infrastructure, and its workforce.

## From fixed routes to dynamic freight networks

Gatik's autonomous vehicle system is designed for regional freight routes covering highways and surface streets. Gatik describes Gatik Driver as its proprietary AI system for autonomous freight. The company's fully driverless trucks operate without a human driver or safety observer on board.

When Gatik and Loblaw announced their initial Toronto fleet in 2020, five vehicles were scheduled to operate on five predetermined routes with fixed pickup and drop-off locations.

By 2022, Gatik's fully driverless Loblaw operation was transporting ambient, refrigerated, and frozen goods from a distribution facility to five nearby stores. Loblaw described the routes as fixed, repetitive, and predictable.

PepsiCo said Gatik's newer deployments can operate across highways and surface streets using dynamic route orchestration for networks spanning hundreds of pickup and drop-off locations.

TechCrunch reported that Gatik began with fixed trips of less than 10 miles but now operates dynamic routes containing dozens of pickup and drop-off points and covering distances of up to 400 miles.

The company has developed its technology around middle-mile freight, where goods move between facilities such as warehouses, distribution centres, and retail locations rather than directly to consumers.

## Scaling AI and autonomous truck production

Gatik also uses simulation and synthetic data to develop and validate its autonomous driving software. In July 2025, the company introduced Arena, an internally developed simulation platform designed to reproduce driving environments without relying exclusively on physical road testing.

Arena generates structured synthetic data that can be used to test autonomous driving behaviour across different conditions. The platform incorporates Nvidia Cosmos world foundation models to generate synthetic driving environments used for training and validation.

Isuzu Motors invested $30 million in Gatik in 2024 as part of a partnership to develop Level 4 autonomous commercial vehicles in North America."""

ARTICLE_BODIES["nvidia-jetson-orin-nano-2"] = """NVIDIA has unveiled the Jetson Orin Nano 2, an edge robotics computer aimed at bringing physical AI to drones, robots, and vision systems. The company is positioning the new board as an entry-level option for developers who want generative AI models running directly on a machine instead of inside a data centre.

NVIDIA's argument for the launch rests on a change in how well small and medium AI models now perform. The company says models of this size have reached the accuracy that only the largest frontier models achieved a year earlier.

Deepu Talla, VP of Robotics and Edge AI at NVIDIA, said: "The Jetson Orin Nano 2 computer puts that breakthrough within reach of millions of developers, delivering the performance and energy efficiency needed for real-time reasoning at the edge."

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

ARTICLE_BODIES["mit-ai-forecasts-extreme-weather"] = """MIT engineers have built an AI tool that forecasts extreme weather without training on historical disaster data.

Kai Chang, a mechanical engineering graduate student, and Professor Themis Sapsis developed the tool. It produces maps of events that have not appeared in a region's historical record but remain statistically-possible. Each map also carries estimates of the event's likely duration and intensity.

## Forecasting extreme weather events without historical precedent

Sapsis holds the William I. Koch Professorship in Mechanical and Ocean Engineering at MIT. Both researchers are affiliated with the MIT Center for Computational Science and Engineering. The pair describe the method, named Extreme Event Aware or eta-learning, in a paper published in Nature Communications on 20 August.

Existing risk models work differently. Insurers, city planners, and grid operators typically want to know what a once-in-a-century storm might look like for a specific location. Current simulations usually depend on datasets that already contain extreme events, learning the conditions that produced them before projecting similar patterns forward.

Chang argues this current approach creates a limit on what such models can show. These methods assume there are very disastrous events that we have seen in the dataset, and they build a method to either estimate the risk of those events, or they try to predict exactly the events that have happened.

Sapsis frames the same limitation through Hurricane Katrina. An event like Hurricane Katrina is something that happens every 30 to 40 years. What will be the Katrina that happens every 100 years? How bad will it be? That is exactly what we are trying to quantify, to help planners prepare for plausible extreme scenarios.

## Combining point statistics with spatial detail

The algorithm works from two types of data. Point statistics capture how often a given intensity level, such as the maximum rainfall recorded across a map, occurs within a dataset. Spatial maps show how an event's impact varies across a region.

Learning the statistical relationship between the two lets the algorithm build spatial patterns for events beyond anything in its training data, without needing prior examples of those exact extremes.

The researchers tested the approach on precipitation across the continental US. They started with 25 years of hourly rainfall data, pooled into daily maps, and computed point statistics describing how often the maximum rainfall on a map reached a given level across that full record.

The training window for the spatial model was narrow. They trained that part of the algorithm using paired low-resolution and high-resolution maps drawn from only the first six months of the 25-year record, a period that contained few or no examples of the heaviest rainfall levels.

## Testing infrastructure against worst-case maps

The highest rainfall ever recorded in New York City measures 200 millimetres. The method can generate plausible maps of a storm that produces 300 millimetres instead, a level with no match in the observational record.

A user can prompt the trained algorithm to show what a once-in-a-century storm might look like for a named city. The output takes the form of maps showing statistically-plausible storms at that frequency.

The generated maps could help a city test its seawall against a storm surge beyond anything recorded. The same maps could show whether the power grid would hold during a longer heatwave, or whether firefighting resources could contain a wildfire larger than any on file.

## Limits of the demonstration so far

Applying the method to a new hazard requires relevant point statistics and spatial data for that specific hazard. The pair point to possible extensions once that data is available.

Sapsis notes that global infrastructure has been optimised for efficiency, leaving little slack in the systems it supports. A single extreme event propagates through supply chains, energy markets, and food systems in weeks. Being able to put a probability on an event that has not happened yet is now a question of national and economic resilience.

The paper was published in Nature Communications on 20 August 2026."""

ARTICLE_BODIES["xpeng-iron-humanoid-robot"] = """XPENG's physical AI unit has secured over $900 million at a $6.3 billion valuation to scale its IRON humanoid robot platform.

The Chinese electric vehicle maker announced the funding round for its robotics business through a set of share purchase agreements with multiple investors. XPENG says the deal represents the largest single-round private capital raise in China's physical AI industry to date.

He Xiaopeng, Chairman and CEO of XPENG, said: "Over the past 12 years, XPENG has remained committed to full-stack in-house R&D, building a solid technological foundation for the physical AI era."

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

IDG Capital said the physical AI industry is moving from technical breakthroughs to scalable manufacturing and commercial deployment. The firm pointed to XPENG's combination of edge AI processors, physical AI foundation models, and complete robotic systems."""

ARTICLE_BODIES["stripe-openrouter-acquisition"] = """Stripe has agreed to acquire OpenRouter, an AI model-routing platform that gives developers access to hundreds of models through a single interface. The deal adds model selection and routing to Stripe's existing work around AI usage and token-based billing.

OpenRouter supports more than 400 models from over 80 providers, according to Stripe. Rather than requiring separate integrations with each model provider, developers can use OpenRouter to send requests through one API.

## Routing beyond model choice

The platform evaluates requests using factors including task complexity, price, speed, and reliability. It can then direct each request to a model suited to those requirements.

OpenRouter also handles a second layer of routing between providers serving the same model. Its documentation says customers can prioritise endpoints based on price, throughput, or latency, while setting requirements such as maximum prices or minimum performance levels.

The platform measures latency and throughput for individual model-provider combinations using rolling performance data. This allows a request to be routed to an endpoint that meets specified cost or performance criteria rather than relying on a fixed provider.

## Multi-model infrastructure expands

Multi-model environments are already common among surveyed organisations. F5's 2026 State of Application Strategy report found that 52% of organisations were chaining or orchestrating multiple AI models, with respondents using an average of seven models.

Menlo Ventures, an OpenRouter investor, reported that 66% of builders upgraded models while staying with their existing provider, while 11% switched vendors.

OpenRouter is also one of several infrastructure providers adding model routing. Snowflake announced dynamic model routing for Cortex AI Gateway on August 18. AWS provides Intelligent Prompt Routing through Bedrock, while Microsoft Foundry offers routing profiles.

## Token usage meets billing

Stripe has also been developing token-based billing tools for AI applications. Its LLM token-billing service can meter consumption according to model and token type, including input, output, and cached tokens where supported.

Enterprise token consumption is already reaching large volumes. Deloitte surveyed 515 US-based business and technology decision-makers in late 2025. The survey found that 37% of respondents were consuming between one billion and 10 billion AI tokens per month, while another 30% were consuming more than 10 billion.

OpenRouter says it processes more than 10 trillion tokens per day across a community of more than 10 million developers and companies."""

ARTICLE_BODIES["amazons-prime-air-drones"] = """Amazon plans to expand its Prime Air drone delivery service to nearly 500 cities and towns across the US by the end of 2026. That build-out amounts to six times the number of locations Prime Air serves today, extending the option to communities with tens of millions of customers.

Reaching that many locations without adding pilots to each flight depends on the drones' own decision-making systems rather than a large ground staff monitoring individual flights. Prime Air's fleet runs on what Amazon calls "highly autonomous" flight software, engineered to keep functioning safely and predictably when something unexpected happens mid-flight.

A Detect-and-Avoid system sits at the centre of that setup, continuously scanning the airspace and surroundings around each drone much like a pilot checking for other aircraft. That scanning lets the drone spot obstacles on its own and make real-time flight decisions without a remote operator stepping in.

## FAA Part 135 certification supports the expansion

Prime Air operates under Federal Aviation Administration Part 135 certification, the licence category used for commercial air carriers. Amazon points to this as the highest tier of FAA oversight available to a drone delivery operation.

The safety systems extend to landing behaviour under adverse conditions. Amazon says its advanced safety systems are built to bring a drone to a safe landing in the event of severe weather or other unexpected events. The drones are also engineered for everyday flying conditions rather than fair-weather use alone.

## Tiered logistics network built around speed

Prime Air carries items weighing five pounds or less that fit in a large shoebox, a limit Amazon says covers more than 60 percent of the items customers most frequently buy on the platform. The eligible catalogue spans millions of items including groceries, cosmetics, medications, and electronics.

Orders can land in as fast as 30 minutes, though Amazon puts the typical wait closer to 60 minutes after checkout. The fee structure ties to Prime status and order size: Prime membership gets drone delivery free on orders of $50 or more, a $2.99 charge applies to smaller Prime orders, and customers without a membership pay $4.99 regardless of basket size.

## Current footprint and what comes next

11 Prime Air sites now cover 10 metro areas across seven states. Arizona's site sits in Tolleson, near Phoenix, and Florida's sits in Ruskin, near Tampa. Kansas City and Baton Rouge each host a single site. Michigan runs two in Hazel Park and Pontiac, both serving the Detroit area.

Amazon reports that Prime Air's drone delivery sites post the highest average delivery volumes of any US drone operation, with thousands of deliveries made daily.

David Carbon, VP of Amazon Prime Air, said: "Customers already turn to Amazon for fast Same- and Next-Day Delivery, and Prime Air provides them an even speedier option when they need it, with deliveries in as fast as 30 minutes."
"""

ARTICLE_BODIES["agentic-ai-in-government-uae"] = """Agentic AI in government just hit the hard part: deciding what a machine may decide.

The UAE government is among the first jurisdictions to formally classify and regulate agentic AI systems in public-sector operations. After deploying AI-assisted tools for document processing, permit routing, and service chatbots, policymakers are now grappling with which decisions can an autonomous agent make on its own, and which require human oversight.

This shift reflects a broader global trend. As agentic systems move from summarising documents to taking actions - booking appointments, initiating payments, allocating resources - the boundary between assistance and authority is blurring.

## Classification frameworks under development

The UAE's approach mirrors frameworks being discussed at the EU and US level. Agentic AI systems are being placed into tiers based on three criteria: autonomy level, impact scope, and intervention capability.

The obvious risk is what happens if one of them cannot pay. Nvidia would lose the sale and the investment at the same time. Kress answers that the hardware finds another buyer.

## Level 2 agents can execute routine tasks

Level 1 agents can suggest actions but must always defer to human approval. Level 2 agents can execute routine tasks within predefined parameters. Level 3 agents can make decisions in non-critical domains but must log all actions for audit.

Levels 4 and 5 represent full autonomy in specific domains, with mandatory oversight boards.

Each pilot operates under strict monitoring protocols, with every agent action logged and reviewed weekly by human supervisors.

## Real-world pilot programs

Several UAE government entities are already running pilot programs with agentic AI:

- Dubai Land Department: An agentic system that can verify property ownership, calculate transfer fees, and draft preliminary sale agreements
- Ministry of Human Resources: An AI agent that assists with visa applications, checking eligibility, gathering required documents
- Abu Dhabi Court of First Instance: A legal research agent that can access case law, summarize relevant precedents

Regulators expect the classification framework to be finalized by early 2027, with pilot programs continuing through the end of 2026. The EU is watching closely."""

# Verify all bodies loaded
for key in ARTICLE_BODIES:
    assert ARTICLE_BODIES[key], f"Empty body for {key}"
print(f"Loaded {len(ARTICLE_BODIES)} article bodies", file=__import__('sys').stderr)
