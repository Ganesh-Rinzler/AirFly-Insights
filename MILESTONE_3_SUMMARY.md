# Milestone 3 Summary: AirFly Insights

This milestone focused on **Route & Airport-Level Analysis** (Week 5) and **Seasonal & Cancellation Analysis** (Week 6), building directly from the analytical foundation established in Milestone 2.

---

## Week 5 — Route & Airport-Level Analysis (`05_route_airport_analysis.ipynb`)

Built a route-level summary table (`route_summary`) and produced six new charts:

- **Chart 21 — Top 10 Origin-Destination Pairs:** Horizontal bar chart of the 10 busiest routes by flight volume (e.g., JFK-LAX, EWR-ORD).
- **Chart 22 — Route Delay Comparison:** Color-coded delay bar chart for the top 10 routes, benchmarked against the fleet average, highlighting underperforming routes.
- **Chart 23 — Airport × Hour Heatmap:** Pivot heatmap showing average departure delay at EWR, JFK, and LGA across all 24 hours — confirming evening congestion (17–21h) as the highest-risk window.
- **Chart 24 — Route Congestion Heatmap:** Top 20 routes × 12 months heatmap, revealing summer congestion peaks on domestic corridors.
- **Chart 25 — Destination Geo-Scatter Map:** Interactive Plotly `scatter_geo` map of all destination airports; bubble size = flight volume, color = avg delay.
- **Chart 26 — Origin Airport On-Time Performance:** 4-panel deep-dive comparing on-time rate, average delay, cancellation rate, and P75/P95 delay tails across EWR, JFK, LGA.

---

## Week 6 — Seasonal & Cancellation Analysis (`06_seasonal_cancellation_analysis.ipynb`)

Since the dataset has no raw cancellation-cause column, proxy methodology was applied — consistent with the delay cause analysis in Week 4.

- **Chart 27 — Monthly Cancellation Trend:** Dual-axis chart (bar = count, line = rate) showing February and June as peak cancellation months.
- **Chart 28 — Day-of-Week Cancellation Rate:** Highlights Monday as the highest cancellation day, suggesting cascading disruptions from weekend operations.
- **Chart 29 — Cancellation Type Proxies:** Stacked bar breaking monthly cancellations into estimated Weather / Carrier / NAS shares, showing weather dominates winter months.
- **Chart 30 — Holiday Period Impact:** Diverging bar charts comparing delay Δ and cancellation Δ vs the annual baseline for Thanksgiving, Christmas, Memorial Day, July 4th, and Labor Day.
- **Chart 31 — Winter Deep-Dive:** 3-panel comparison (cancel rate, avg delay, delay rate + P95) for December, January, and February against annual averages.
- **Chart 32 — Seasonal Violin Plot:** Full distribution shape across all four seasons using violin plots with quartile (IQR) lines and mean markers.

---

## Streamlit Dashboard Updates (`app.py`)

| Change | Details |
|---|---|
| 2 new pages added | 🛫 Route & Airport Deep Dive, ❌ Cancellation & Seasonal Analysis |
| Sidebar redesign | Emoji icons on all pages, About expander, Milestone 3 caption |
| Insight callouts | `st.expander("💡 Key Insight")` after major charts |
| Data note banner | `st.info()` on cancellation page explaining proxy methodology |
| Airport coordinate lookup | `AIRPORT_COORDS` dict added for geo-scatter map |

---

**Status:** Milestone 3 (Weeks 5–6) complete. Dashboard now has 7 pages covering all analyses from MS2 and MS3.
