# Milestone 4 Summary: AirFly Insights

This milestone delivered the **final, product-grade version** of the AirFly Insights platform — migrating from Streamlit to **Plotly Dash**, consolidating all 7 analysis pages into 5 focused narrative views, and introducing the **Smart Flight Planner** as a user-centric decision-support tool.

---

## Dashboard Rebuild — Plotly Dash (`dashboard.py`)

The Streamlit application (`app.py`) was fully replaced with a custom Plotly Dash implementation featuring a bespoke dark-mode design system.

### Architecture Changes

| Area | Milestone 3 (Streamlit) | Milestone 4 (Dash) |
|---|---|---|
| Framework | Streamlit | Plotly Dash + Flask |
| Pages | 7 pages | 5 focused pages |
| Charts | Static matplotlib/seaborn images | Native interactive Plotly figures |
| Layout engine | Streamlit columns | Custom CSS grid (`assets/style.css`) |
| Sidebar | Streamlit sidebar | Custom fixed HTML sidebar |
| Design system | Streamlit defaults | Hand-crafted dark-mode CSS tokens |

### 5 Narrative Pages

| Page | Route | Question it answers |
|---|---|---|
| **Overview** | `/` | What is the scale and performance of NYC flight operations? |
| **Delay Analysis** | `/delays` | When should I fly, and which airline should I avoid? |
| **Temporal Trends** | `/trends` | How do delays evolve over time across the year? |
| **Routes & Airports** | `/routes` | Where does NYC fly, and which airport performs better? |
| **Seasonal & Cancellations** | `/seasonal` | Which months and seasons are the most disruptive? |

---

## Smart Flight Planner (`/planner`)

The flagship feature of Milestone 4 — a fully interactive recommendation engine that answers the traveler's core question: *"Which airline, airport, day, and time should I choose to minimize delays?"*

### Inputs
- **Destination Airport**: Dropdown of all 105 served airports
- **Travel Month**: January through December
- **Delay Tolerance**: Slider from 0–60 minutes (step 5)

### Engine Logic
1. Filters the 336,776-flight dataset to the selected destination + month.
2. Groups by `origin × airline × day_of_week × dep_hour_bin` — computing per-combination on-time rate and average delay.
3. Ranks all combinations by on-time rate (primary) and average delay (secondary).
4. Returns the **top 5 ranked combinations**, each tagged with a **Low / Medium / High risk score** based on average delay thresholds (<10 min / <20 min / ≥20 min).

### Outputs
- **Best Match Hero Card**: Instant summary of the top recommendation with risk badge and on-time percentage.
- **Top 5 Recommendation Cards**: Each showing origin → destination, airline, day, time slot, on-time rate, and average delay.
- **On-Time Rate Comparison Chart**: Interactive horizontal bar chart (green-to-red gradient).
- **Average Delay Comparison Chart**: Interactive horizontal bar chart (green-to-red gradient).
- **Insight Callout**: Footer noting sample size and tolerance definition used.

---

## Design System (`assets/style.css`)

A custom CSS design system was authored to achieve a professional, product-grade aesthetic:

- **Dark-mode palette**: `#0f172a` base, `#1e293b` surface, `#3b82f6` accent blue.
- **Component tokens**: `.kpi-card`, `.dash-card`, `.rec-card`, `.rec-card-best`, `.risk-badge`, `.risk-badge-lg`, `.planner-hero`, `.result-summary-card`.
- **Responsive grid utilities**: `.kpi-grid` (4-column), `.chart-grid-2` (2-column).
- **Sidebar**: Fixed-width dark panel with active state highlighting and brand identity footer.
- **Typography**: Inter font with consistent size scale across KPI values, labels, and callouts.

---

## Modular Source Code (`src/`)

| File | Purpose |
|---|---|
| `data_loader.py` | Optimized CSV ingestion with module-level caching (`_df_cache`) to avoid repeated disk reads |
| `config.py` | `SEASON_MAP`, `MONTH_NAMES`, `DAY_ORDER`, airport coordinate lookups, and system constants |
| `utils.py` | Reusable chart helper functions and coordinate lookups |
| `features.py` | Feature engineering pipeline (route, delay severity, temporal bins) |

---

The platform has been transformed from an exploratory Streamlit prototype into a polished, decision-support Dash application backed by 336,776 historical flights. All five pages are live and the Smart Flight Planner is fully operational at **http://127.0.0.1:8050**.
