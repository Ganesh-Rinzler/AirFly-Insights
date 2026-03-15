# AirFly Insights - Milestone 2 Project Review

This document provides a comprehensive review of the analytical work completed for **AirFly Insights** up to Milestone 2. It covers data exploration, preprocessing, feature engineering, visual analysis, and deep delay intelligence.

---

## 1. Project Overview & Objectives
The goal of Milestone 2 was to transform raw flight data into actionable insights, focusing on operational performance and flight disruptions (delays and cancellations) at NYC's major airports (EWR, JFK, LGA) in 2013.

---

## 2. Notebook-by-Notebook Analysis

### 2.1. Data Exploration (`01_data_exploration.ipynb`)
**Focus**: Understanding the raw dataset and optimizing resources.
- **Initialization**: Defined project KPIs focusing on volume, reliability, and punctuality.
- **Data Loading**: Loaded the census-level flights dataset.
- **Schema & Types**: Explored column definitions (tailnum, carrier, origin, dest, etc.).
- **Data Integrity**: Identified significant null values in arrival/departure times, correlating them with flight cancellations.
- **Memory Optimization**: Reduced the memory footprint by ~70% using downcasting to `int8/int16` and converting strings to `categorical` types.

### 2.2. Preprocessing & Feature Engineering (`02_preprocessing_feature_engineering.ipynb`)
**Focus**: Cleaning data and deriving analytical dimensions.
- **Null Handling**: Created the `is_cancelled` flag to separate operational disruptions from missing data.
- **Datetime Engineering**: Parsed `time_hour` to extract `date`, `month`, `day_of_week`, and `week_of_year`.
- **Route Creation**: Derived a unique `route` feature by concatenating `origin` and `dest`.
- **Performance Metrics**:
    - `dep_hour_bin`: Categorized flights into 'Morning', 'Afternoon', 'Evening', and 'Night'.
    - `is_delayed`: A binary flag for flights with >15 min departure delay.
    - `delay_severity`: Bucketed delays into groups (On Time, Minor, Moderate, Severe, Extreme).
    - `speed_mph`: Calculated using flight distance and air time.

### 2.3. Visual Analysis (`03_visual_analysis.ipynb`)
**Focus**: Uncovering initial patterns through visualization.
- **Operational Volume**: Identified United (UA) and JetBlue (B6) as top carriers.
- **Temporal Volume**: Visualized monthly peaks in summer and holiday seasons.
- **Delay Distribution**: Analyzed the "long tail" of flight delays, showing that while most flights are near on-time, extreme outliers significantly impact average performance.
- **Airport Comparison**: Compared the operational throughput across EWR, JFK, and LGA.

### 2.4. Delay Analysis & Temporal Intelligence (`04_delay_analysis.ipynb`)
**Focus**: Advanced statistical analysis and cause investigation.
- **Seasonal Comparison**: Compared delay severity distributions as proxies for seasonal weather impacts (Winter vs. Summer).
- **Carrier Benchmarking**: Analyzed excess delay per carrier relative to the fleet average to isolate airline-specific operational issues.
- **Temporal Decomposition**:
    - **7-day/30-day Rolling Averages**: Smoothed out daily noise to identify underlying performance trends.
    - **Daily Delay Rates**: Visualized the percentage of daily flights delayed by more than 15 minutes.
- **Congestion Mapping**: Used heatmaps (Hour vs. Day of Week) to pinpoint high-risk congestion windows (e.g., late Thursday/Friday afternoons).

---

## 3. Delay Analysis Approach: The Methodology
Our approach to delay analysis is multi-layered:
1.  **Cancellations as a Metric**: Instead of dropping nulls, we treat them as the most severe form of disruption.
2.  **Delay Severity Bucketing**: We move beyond simple averages to understand the "severity" of late flights, which is more relevant for airline scheduling and passenger experience.
3.  **Proxy Analysis**: Since "cause of delay" data is missing, we use **Temporal Proxies** (winter storms, summer thunderstorms) and **Carrier Proxies** (efficiency vs. fleet average) to infer root causes.
4.  **Trend Awareness**: Using rolling averages allows us to see if performance is improving or deteriorating over time, filtering out "bad weather days."

---

## 4. Streamlit Dashboard: Interactive Insights
The companion Streamlit dashboard (`app.py`) provides an interactive interface for stakeholders to explore these findings.

### Dashboard Pages & Features
- **Overview & KPIs**: Real-time summary metrics (Total Flights, On-Time Rate, Avg Delay).
- **Delay Analysis**: Interactive severity charts and airline-specific performance toggles.
- **Temporal Trends**: Date-range exploration of 7-day and 30-day rolling averages.
- **Route & Airport Explorer**: Drill-down into specific origin-destination pairs and airport performance.
- **Weather & Seasonal Insights**: Comparisons between peak summer operations and potentially winter-impacted months.

---

## 5. Conclusion
Milestone 2 has successfully established a robust data pipeline and a deep analytical foundation. We now have the tools to predict potential disruptions and optimize carrier selection based on historical performance patterns.
