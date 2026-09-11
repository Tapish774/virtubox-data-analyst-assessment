# Slide 1: Business Context & Objective
* **Title:** Marketplace Logistics & Customer Retention Diagnosis
* **Audience:** Senior Business Management
* **Core Problem:** Escalating fulfillment delays hurting customer reviews and platform retention.
* **Goal:** Identify operational delivery bottlenecks and quantify their direct impact on marketplace growth and repeat revenue.

# Slide 2: Data Scope & Pipeline
* **Source:** Brazilian E-Commerce Public Dataset (Olist).
* **Volume:** 99,441 orders, 112,650 order items across 9 relational tables.
* **Methodology:** Cleaned via Python (Pandas), deduplicated multiple review records, derived actual delivery durations and SLA variance, and mapped repeat buyers via unique customer tokens.

# Slide 3: Executive Platform Health Summary
* **Total GMV:** $13.59M across 73 product categories.
* **On-Time Delivery Rate:** 91.9% platform-wide.
* **Repeat Purchase Rate:** 3.12% (96.88% of buyers purchase only once).
* **Average Review Score:** 4.08 / 5.0 baseline.

# Slide 4: Deep-Dive: Delivery Delay vs. CSAT Collapse
* **Finding:** Delivery SLA breach is the #1 driver of negative customer reviews.
* **The Data:** On-time orders average 4.27/5.0 stars; delayed orders drop 60.6% to 1.68/5.0 stars.
* **Operational Flaw:** Small, lightweight electronics suffer 14.2% delay rates compared to only 7.8% for bulk furniture, caused by overly tight algorithm estimates rather than courier transport failure.

# Slide 5: Strategic Recommendations
* **1. Dynamic SLA Buffer Calibration:** Retrain delivery estimate engines on 85th-percentile regional transit history rather than flat averages.
* **2. Automated Post-Purchase CRM:** Trigger customized category cross-sell workflows 21 days post-delivery.
* **3. Regional 3PL Cross-Docks:** Contract regional fulfillment centers in Northeast hubs to address transit times that currently average 21-28 days.

# Slide 6: Expected Business Impact & KPIs
* **Customer Retention:** Target increasing the repeat purchase rate from 3.12% to 6.0% within 6 months.
* **CSAT Protection:** Reduce delivery SLA breaches by 45%, raising average platform review scores to 4.35+.
* **Primary Metrics:** SLA breach rate (<4%), transit duration across interstate routes, and 60-day repeat buyer retention rate.

# Slide 7: Analytical Limitations & Next Steps
* **Limitations:** Dataset lacks advertising spend (CAC) and merchant cost-of-goods-sold (COGS), restricting unit economics to GMV.
* **Next Steps:** Ingest pre-purchase funnel telemetry (cart abandonment rates) and carrier invoice costs to evaluate net profit margins per SKU.
