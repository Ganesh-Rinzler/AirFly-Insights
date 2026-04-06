# Milestone 1 Summary: AirFly Insights

This milestone focused on **Data Exploration** (Week 1) — understanding the raw nycflights13 dataset, identifying structural characteristics, and laying the analytical foundation for all subsequent milestones.

---

## Week 1 — Data Exploration (`01_data_exploration.ipynb`)

### Dataset Overview

The dataset contains **336,776 flight records** departing from the three major New York City airports — EWR (Newark), JFK (John F. Kennedy), and LGA (LaGuardia) — across the entire calendar year **2013**. It includes 19 original variables covering schedule timing, carrier identity, route geography, and flight performance.

### Key Exploration Activities

- **Schema Inspection**: Loaded the raw `flights` table and catalogued all 19 columns — identifying data types, value ranges, and semantic groupings (temporal, operational, geographic).
- **Null Value Analysis**: Detected missing values in `dep_time`, `arr_time`, `dep_delay`, `arr_delay`, and `air_time`. Identified that these NaNs correspond to **cancelled flights**, not random missingness — a critical finding for later preprocessing.
- **Airline & Route Distribution**: Counted unique carriers (16 airlines) and origin-destination pairs (105 distinct airports served). Identified the dominant carriers by flight volume and the busiest departure airports.
- **Temporal Coverage**: Confirmed complete coverage across all 12 months of 2013 with no structural gaps, and observed monthly seasonality in flight volumes.
- **Flight Corridor Mapping**: Identified the top origin–destination corridors from NYC, with JFK–LAX and EWR–ORD among the highest-frequency routes.
- **Initial Statistics**: Computed summary statistics for key numeric fields (`dep_delay`, `arr_delay`, `distance`, `air_time`) — revealing heavy right-skew in delay distributions and a broad distance range (17 to 4,983 miles).

### Key Findings from EDA

| Observation | Detail |
|---|---|
| Total flights | 336,776 |
| Cancelled flights | ~8,000+ (identified by NaN dep_time) |
| Unique airlines | 16 carriers |
| Airports served | 105 destinations across the USA |
| Avg departure delay | ~13 min (including delays only) |
| Busiest origin | EWR (Newark Liberty) |
| Heaviest travel months | June, July, August |

---


