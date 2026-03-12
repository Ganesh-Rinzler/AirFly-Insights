# AirFly Insights: Interactive Flight Operations Dashboard

AirFly Insights is a comprehensive data analysis system and interactive dashboard designed to explore large-scale airline flight data. By uncovering operational trends, delay patterns, and cancellation causes, it provides actionable insights for airline operators and analysts.

## 🚀 Key Features

- **Milestone 1 & 2**: Data Preprocessing, Feature Engineering, and initial visual exploration of flight delays.
- **Milestone 3: Advanced Analytics**:
    - **Route & Airport Deep Dive**: Analysis of top 10 O-D pairs, route congestion heatmaps, and geographic delay distribution.
    - **Cancellation & Seasonal Trends**: Monthly and day-of-week cancellation rates, holiday impact analysis, and winter performance deep-dives.
- **Interactive Dashboard**: A dedicated Streamlit application for real-time data exploration and visualization.

## 📁 Project Structure

- **`app.py`**: The main entry point for the Streamlit dashboard.
- **`notebooks/`**: Comprehensive Jupyter notebooks for each phase of analysis (Weeks 1-6).
- **`src/`**: Modularized source code for data loading, processing, and visualization utilities.
- **`data/`**: Processed datasets (CSV/Parquet format).
- **`outputs/figures/`**: Exported static charts and interactive HTML plots.
- **`MILESTONE_3_SUMMARY.md`**: Detailed technical summary of the latest analysis phase.

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- Required libraries listed in `requirements.txt`

### Installation

1. Clone the repository and navigate to the project root.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboard

To launch the interactive dashboard, run the following command from the project root:

```bash
python -m streamlit run app.py
```

The app will typically be available at `http://localhost:8501`.

### Data Exploration

Detailed analyses can be found in the `notebooks/` directory:
- `05_route_airport_analysis.ipynb`: Route performance and airport congestion.
- `06_seasonal_cancellation_analysis.ipynb`: Seasonal patterns and cancellation deep-dives.

---
*Developed for the AirFly Insights MS2 project.*

