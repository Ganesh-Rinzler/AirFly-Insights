# Milestone 2 Summary: AirFly Insights

This milestone focused on transforming the raw NYC Flights 2013 data into a structured format suitable for advanced analysis and creating initial visualizations to uncover operational trends.

## 1. Data Preprocessing (Week 2)
The primary goal was to handle data quality issues and prepare the temporal features.

*   **Null Value Management**: Identified that missing values in arrival/departure times correspond to cancelled flights. Created a dedicated `is_cancelled` flag to preserve these records for cancellation rate analysis.
*   **Datetime Standardization**: Parsed the `time_hour` column and expanded it into granular features: `date`, `day_of_week`, `day_name`, and `week_of_year`.
*   **Data Integrity**: Verified the final preprocessed dataset and saved it as `flights_processed.csv` for high-performance reuse in subsequent notebooks.

## 2. Feature Engineering (Week 2)
New analytical dimensions were derived to capture flight performance and operational context.

*   **Route Identification**: Combined `origin` and `dest` to create a `route` feature (e.g., 'JFK-LAX').
*   **Temporal Binning**: Categorized departure times into operational periods: 'Morning', 'Afternoon', 'Evening', and 'Night'.
*   **Performance Metrics**: 
    *   Calculated `total_delay` (Departure + Arrival delay).
    *   Computed `speed_mph` using flight distance and air time.
*   **Categorical Flags**:
    *   `is_delayed`: Positive for departures delayed by more than 15 minutes.
    *   `is_early`: Positive for departures more than 5 minutes early.
*   **Delay Severity**: Implemented a classification system ranging from 'On Time / Early' to 'Extreme (>3 hrs)'.

## 3. Visual Analysis (Week 3)
Performed comprehensive exploratory data analysis (EDA) using the newly engineered features.

*   **Operational Volume**: Visualized the top airlines, busiest routes, and flight distributions across NYC's three major airports (EWR, JFK, LGA).
*   **Temporal Trends**: Analyzed flight volumes and average delays across different months and days of the week.
*   **Statistical Distributions**: Used histograms and boxplots to understand the distribution of delays and identify outliers.
*   **Correlation & Comparison**: Investigated the relationship between airline performance and delay rates using multi-variate bar charts.

## 4. Delay Analysis & Temporal Intelligence (Week 4)
This phase involved deeper statistical analysis and temporal modeling to understand the root causes of flight disruptions.

*   **Delay Cause Proxies**: Since explicit cause data (weather, carrier, NAS) wasn't available, temporal and carrier-based proxies were developed. 
    *   **Weather Proxy**: Analyzed seasonal peaks (Winter/Summer) to infer weather-related impacts.
    *   **Carrier Proxy**: Evaluated excess delay per carrier relative to fleet averages.
*   **Temporal Trend Decomposition**: Applied rolling averages to smooth daily volatility and identify underlying cyclic patterns.
*   **Advanced Distributions**: Utilized log-transformations and normalization to analyze skewed delay distributions.
*   **Complex Visualizations**: Created advanced heatmaps for congestion analysis and violin plots to compare delay density across categories.

## 5. Documentation
*   **Feature Dictionary**: Developed a comprehensive guide explaining both original and engineered columns to ensure transparency for stakeholders.

---
**Status**: Milestone 2 (Weeks 2-4) is fully documented. The project is positioned for final refinement or deployment.
