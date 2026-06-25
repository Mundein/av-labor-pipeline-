# Autonomous Vehicle (AV) Labor Planning & Adherence Pipeline

An end-to-end data pipeline that simulates, processes, and visualizes daily fleet labor distribution and shift targets across multiple regional markets.

## 📊 Live Interactive Dashboard
👉 **[View the Live Looker Studio Dashboard](https://datastudio.google.com/reporting/c27ff0a0-cd10-4095-9357-bff9b829dbf8)**

## 🛠️ Tech Stack & Architecture
1. **Data Generation (Python / Pandas):** Simulates granular daily shift logs, deliberately engineering real-world edge-case data anomalies (case mismatches, missing employee IDs, duplicates).
2. **Data Warehousing & Modeling (BigQuery):** 
   * Orchestrates an initial staging cleanup to cast data types seamlessly.
   * Runs a conditional baseline script (`CASE WHEN`) to dynamically map out headcount targets by specific market and operational roles.
3. **Data Blending & Visualization (Looker Studio):** Utilizes Looker Studio's native blending layer to cross-reference daily logs against targets, tracking real-time schedule adherence and headcount gaps.

## 🗄️ Repository Structure
* `labor_data_extraction.py` - Core Python data simulation script
* `clean_daily_labor_summary.sql` - BigQuery data-type casting and staging script
* `daily_targets_generator.sql` - BigQuery script mapping operational baselines
* `output.csv` - Raw generated dataset output
