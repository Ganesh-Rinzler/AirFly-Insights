"""
AirFly Insights — Streamlit Dashboard
Interactive visualization of NYC Flights 2013 data.
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─── Page Config ───
st.set_page_config(
    page_title="AirFly Insights",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Constants ───
SEASON_MAP = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall'
}
SEASON_ORDER = ['Winter', 'Spring', 'Summer', 'Fall']
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DAY_ORDER = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


@st.cache_data
def load_data():
    """Load and prepare the processed flights data."""
    df = pd.read_csv('data/processed/flights_processed.csv', low_memory=False)
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['season'] = df['month'].map(SEASON_MAP)
    return df


# ─── Load Data ───
df = load_data()
df_completed = df[df['is_cancelled'] == 0].copy()

# ─── Sidebar Navigation ───
st.sidebar.title("AirFly Insights")
st.sidebar.markdown("NYC Flights 2013 Analysis")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["Overview & KPIs", "Delay Analysis", "Temporal Trends",
     "Route & Airport Explorer", "Weather & Seasonal Insights"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Filters**")
selected_origins = st.sidebar.multiselect(
    "Origin Airport", options=['EWR', 'JFK', 'LGA'],
    default=['EWR', 'JFK', 'LGA']
)
selected_seasons = st.sidebar.multiselect(
    "Season", options=SEASON_ORDER, default=SEASON_ORDER
)

# Apply filters
mask = (df['origin'].isin(selected_origins)) & (df['season'].isin(selected_seasons))
df_filtered = df[mask]
df_comp_filtered = df_filtered[df_filtered['is_cancelled'] == 0]


# ════════════════════════════════════════
# PAGE 1: Overview & KPIs
# ════════════════════════════════════════
if page == "Overview & KPIs":
    st.title("Overview & Key Performance Indicators")
    st.markdown("High-level summary of NYC flight operations in 2013.")

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)
    total_flights = len(df_filtered)
    completed = len(df_comp_filtered)
    on_time_pct = (1 - df_comp_filtered['is_delayed'].mean()) * 100 if len(df_comp_filtered) > 0 else 0
    cancel_rate = df_filtered['is_cancelled'].mean() * 100
    avg_delay = df_comp_filtered['dep_delay'].mean() if len(df_comp_filtered) > 0 else 0

    col1.metric("Total Flights", f"{total_flights:,}")
    col2.metric("On-Time Rate", f"{on_time_pct:.1f}%")
    col3.metric("Avg Departure Delay", f"{avg_delay:.1f} min")
    col4.metric("Cancellation Rate", f"{cancel_rate:.2f}%")

    st.markdown("---")

    # Monthly flight volume
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Monthly Flight Volume")
        monthly = df_filtered.groupby('month').size().reset_index(name='flights')
        monthly['month_name'] = monthly['month'].apply(lambda m: MONTH_NAMES[m - 1])
        fig = px.line(monthly, x='month_name', y='flights', markers=True,
                      labels={'month_name': 'Month', 'flights': 'Number of Flights'})
        fig.update_traces(line=dict(width=3, color='steelblue'), marker=dict(size=8))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Top 10 Airlines by Flight Count")
        top_airlines = df_filtered.groupby('name').size().nlargest(10).reset_index(name='flights')
        fig = px.bar(top_airlines, x='flights', y='name', orientation='h',
                     color='flights', color_continuous_scale='Blues',
                     labels={'name': 'Airline', 'flights': 'Flights'})
        fig.update_layout(height=400, yaxis={'categoryorder': 'total ascending'},
                          coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    # Origin airport split
    st.subheader("Flights by Origin Airport")
    origin_counts = df_filtered.groupby('origin').size().reset_index(name='flights')
    fig = px.pie(origin_counts, values='flights', names='origin',
                 color='origin', color_discrete_map={'EWR': '#3498db', 'JFK': '#2ecc71', 'LGA': '#e74c3c'})
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════
# PAGE 2: Delay Analysis
# ════════════════════════════════════════
elif page == "Delay Analysis":
    st.title("Delay Analysis")
    st.markdown("Deep dive into departure delay patterns, carrier performance, and delay severity.")

    # Delay distribution
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Departure Delay Distribution")
        delays = df_comp_filtered['dep_delay'].dropna().clip(-60, 300)
        fig = px.histogram(delays, nbins=80, labels={'value': 'Departure Delay (min)'},
                           color_discrete_sequence=['steelblue'])
        fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="On time")
        fig.add_vline(x=15, line_dash="dash", line_color="orange", annotation_text="15 min")
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Delay Severity Breakdown")
        severity = df_filtered['delay_severity'].value_counts().reset_index()
        severity.columns = ['severity', 'count']
        fig = px.pie(severity, values='count', names='severity',
                     color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Average delay by carrier
    st.subheader("Average Departure Delay by Airline")
    carrier_delay = (df_comp_filtered.groupby('name')['dep_delay']
                     .mean().sort_values().reset_index())
    carrier_delay.columns = ['Airline', 'Avg Delay (min)']
    colors = ['#e74c3c' if v > 15 else '#f39c12' if v > 5 else '#2ecc71'
              for v in carrier_delay['Avg Delay (min)']]
    fig = go.Figure(go.Bar(
        x=carrier_delay['Avg Delay (min)'], y=carrier_delay['Airline'],
        orientation='h', marker_color=colors
    ))
    fig.add_vline(x=15, line_dash="dash", line_color="red")
    fig.update_layout(height=500, xaxis_title='Average Departure Delay (min)',
                      yaxis_title='')
    st.plotly_chart(fig, use_container_width=True)

    # Heatmap: Hour x Day of Week
    st.subheader("Delay Heatmap: Hour × Day of Week")
    heatmap_data = df_comp_filtered.pivot_table(
        values='dep_delay', index='hour', columns='day_name', aggfunc='mean'
    ).reindex(columns=DAY_ORDER)

    fig = px.imshow(heatmap_data, color_continuous_scale='YlOrRd', aspect='auto',
                    labels={'x': 'Day of Week', 'y': 'Hour', 'color': 'Avg Delay (min)'})
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════
# PAGE 3: Temporal Trends
# ════════════════════════════════════════
elif page == "Temporal Trends":
    st.title("Temporal Trends & Rolling Averages")
    st.markdown("Explore how delays evolve over time using rolling averages and trend decomposition.")

    # Daily delay with rolling averages
    daily = df_comp_filtered.groupby('date').agg(
        avg_delay=('dep_delay', 'mean'),
        delay_rate=('is_delayed', 'mean')
    ).sort_index()
    daily.index = pd.to_datetime(daily.index)
    daily['rolling_7d'] = daily['avg_delay'].rolling(7, min_periods=1).mean()
    daily['rolling_30d'] = daily['avg_delay'].rolling(30, min_periods=1).mean()

    st.subheader("Daily Departure Delay with Rolling Averages")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=daily.index, y=daily['avg_delay'], mode='lines',
                             name='Daily Average', line=dict(color='lightsteelblue', width=1),
                             opacity=0.5))
    fig.add_trace(go.Scatter(x=daily.index, y=daily['rolling_7d'], mode='lines',
                             name='7-Day Rolling Mean', line=dict(color='#e74c3c', width=2.5)))
    fig.add_trace(go.Scatter(x=daily.index, y=daily['rolling_30d'], mode='lines',
                             name='30-Day Rolling Mean', line=dict(color='#2c3e50', width=3, dash='dash')))
    fig.update_layout(height=450, yaxis_title='Avg Departure Delay (min)',
                      xaxis_title='Date', hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Rolling delay rate
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Rolling Delay Rate (7-Day)")
        daily['delay_rate_7d'] = daily['delay_rate'].rolling(7, min_periods=1).mean() * 100
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=daily.index, y=daily['delay_rate_7d'], fill='tozeroy',
                                 line=dict(color='#e74c3c', width=2), name='7-Day Rolling'))
        overall_rate = df_comp_filtered['is_delayed'].mean() * 100
        fig.add_hline(y=overall_rate, line_dash="dash", line_color="black",
                      annotation_text=f"Avg: {overall_rate:.1f}%")
        fig.update_layout(height=400, yaxis_title='Delay Rate (%)')
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("Monthly Dep vs Arr Delay")
        monthly_d = df_comp_filtered.groupby('month').agg(
            dep=('dep_delay', 'mean'), arr=('arr_delay', 'mean')
        ).reset_index()
        monthly_d['month_name'] = monthly_d['month'].apply(lambda m: MONTH_NAMES[m - 1])
        fig = go.Figure()
        fig.add_trace(go.Bar(x=monthly_d['month_name'], y=monthly_d['dep'],
                             name='Departure Delay', marker_color='#3498db'))
        fig.add_trace(go.Bar(x=monthly_d['month_name'], y=monthly_d['arr'],
                             name='Arrival Delay', marker_color='#e74c3c', opacity=0.6))
        fig.update_layout(height=400, barmode='group', yaxis_title='Avg Delay (min)')
        st.plotly_chart(fig, use_container_width=True)

    # Cancellation rate rolling
    st.subheader("Daily Cancellation Rate (7-Day Rolling)")
    daily_all = df_filtered.groupby('date').agg(
        total=('is_cancelled', 'count'), cancelled=('is_cancelled', 'sum')
    ).sort_index()
    daily_all.index = pd.to_datetime(daily_all.index)
    daily_all['cancel_rate'] = daily_all['cancelled'] / daily_all['total'] * 100
    daily_all['cancel_7d'] = daily_all['cancel_rate'].rolling(7, min_periods=1).mean()

    fig = go.Figure()
    fig.add_trace(go.Bar(x=daily_all.index, y=daily_all['cancel_rate'],
                         name='Daily Rate', marker_color='#e74c3c', opacity=0.3))
    fig.add_trace(go.Scatter(x=daily_all.index, y=daily_all['cancel_7d'], mode='lines',
                             name='7-Day Rolling', line=dict(color='#c0392b', width=2.5)))
    fig.update_layout(height=400, yaxis_title='Cancellation Rate (%)')
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════
# PAGE 4: Route & Airport Explorer
# ════════════════════════════════════════
elif page == "Route & Airport Explorer":
    st.title("Route & Airport Explorer")
    st.markdown("Explore the busiest routes and compare origin airport performance.")

    # Carrier filter (page-specific)
    all_carriers = sorted(df_filtered['name'].dropna().unique())
    selected_carriers = st.multiselect("Filter by Airline", options=all_carriers, default=[])
    if selected_carriers:
        df_page = df_filtered[df_filtered['name'].isin(selected_carriers)]
        df_comp_page = df_page[df_page['is_cancelled'] == 0]
    else:
        df_page = df_filtered
        df_comp_page = df_comp_filtered

    # Top routes
    st.subheader("Top 15 Busiest Routes")
    top_routes = df_page.groupby('route').size().nlargest(15).reset_index(name='flights')
    fig = px.bar(top_routes, x='flights', y='route', orientation='h',
                 color='flights', color_continuous_scale='Viridis',
                 labels={'route': 'Route', 'flights': 'Flights'})
    fig.update_layout(height=500, yaxis={'categoryorder': 'total ascending'},
                      coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Origin airport comparison
    st.subheader("Origin Airport Comparison")
    col1, col2, col3 = st.columns(3)

    origin_stats = df_page.groupby('origin').agg(
        flights=('is_cancelled', 'count'),
        cancel_rate=('is_cancelled', 'mean')
    )
    origin_delay = df_comp_page.groupby('origin')['dep_delay'].mean()

    with col1:
        st.markdown("**Flight Volume**")
        fig = px.bar(origin_stats.reset_index(), x='origin', y='flights',
                     color='origin', color_discrete_map={'EWR': '#3498db', 'JFK': '#2ecc71', 'LGA': '#e74c3c'})
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**Avg Departure Delay**")
        od = origin_delay.reset_index()
        od.columns = ['origin', 'delay']
        fig = px.bar(od, x='origin', y='delay',
                     color='origin', color_discrete_map={'EWR': '#3498db', 'JFK': '#2ecc71', 'LGA': '#e74c3c'})
        fig.update_layout(height=300, showlegend=False, yaxis_title='Avg Delay (min)')
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown("**Cancellation Rate**")
        cr = origin_stats[['cancel_rate']].reset_index()
        cr['cancel_rate'] = cr['cancel_rate'] * 100
        fig = px.bar(cr, x='origin', y='cancel_rate',
                     color='origin', color_discrete_map={'EWR': '#3498db', 'JFK': '#2ecc71', 'LGA': '#e74c3c'})
        fig.update_layout(height=300, showlegend=False, yaxis_title='Cancel Rate (%)')
        st.plotly_chart(fig, use_container_width=True)

    # Delay by route (top 10)
    st.subheader("Average Delay by Route (Top 10 Busiest)")
    top10_routes = df_comp_page.groupby('route').size().nlargest(10).index
    route_delay = (df_comp_page[df_comp_page['route'].isin(top10_routes)]
                   .groupby('route')['dep_delay'].mean()
                   .sort_values().reset_index())
    route_delay.columns = ['Route', 'Avg Delay (min)']
    fig = px.bar(route_delay, x='Avg Delay (min)', y='Route', orientation='h',
                 color='Avg Delay (min)', color_continuous_scale='RdYlGn_r')
    fig.update_layout(height=400, coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════
# PAGE 5: Weather & Seasonal Insights
# ════════════════════════════════════════
elif page == "Weather & Seasonal Insights":
    st.title("Weather & Seasonal Insights")
    st.markdown("Analyze how seasons and weather patterns affect flight delays and cancellations.")

    # Seasonal delay comparison
    st.subheader("Seasonal Delay Comparison")
    season_stats = df_comp_filtered.groupby('season').agg(
        avg_delay=('dep_delay', 'mean'),
        delay_rate=('is_delayed', 'mean')
    ).reindex(SEASON_ORDER)
    season_cancel = df_filtered.groupby('season')['is_cancelled'].mean().reindex(SEASON_ORDER) * 100

    col1, col2, col3 = st.columns(3)
    season_colors_map = {'Winter': '#3498db', 'Spring': '#2ecc71', 'Summer': '#e74c3c', 'Fall': '#f39c12'}

    with col1:
        st.markdown("**Avg Departure Delay**")
        sd = season_stats[['avg_delay']].reset_index()
        fig = px.bar(sd, x='season', y='avg_delay',
                     color='season', color_discrete_map=season_colors_map,
                     category_orders={'season': SEASON_ORDER})
        fig.update_layout(height=350, showlegend=False, yaxis_title='Avg Delay (min)')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**Delay Rate (>15 min)**")
        dr = season_stats[['delay_rate']].reset_index()
        dr['delay_rate'] = dr['delay_rate'] * 100
        fig = px.bar(dr, x='season', y='delay_rate',
                     color='season', color_discrete_map=season_colors_map,
                     category_orders={'season': SEASON_ORDER})
        fig.update_layout(height=350, showlegend=False, yaxis_title='Delay Rate (%)')
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown("**Cancellation Rate**")
        sc = season_cancel.reset_index()
        sc.columns = ['season', 'cancel_rate']
        fig = px.bar(sc, x='season', y='cancel_rate',
                     color='season', color_discrete_map=season_colors_map,
                     category_orders={'season': SEASON_ORDER})
        fig.update_layout(height=350, showlegend=False, yaxis_title='Cancel Rate (%)')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Delay severity by season (stacked)
    st.subheader("Delay Severity Distribution by Season")
    severity_season = pd.crosstab(df_filtered['season'], df_filtered['delay_severity'],
                                  normalize='index') * 100
    severity_season = severity_season.reindex(index=SEASON_ORDER)

    fig = go.Figure()
    severity_colors = {
        'On Time': '#2ecc71', 'Minor Delay': '#f1c40f', 'Moderate Delay': '#e67e22',
        'Severe Delay': '#e74c3c', 'Extreme Delay': '#8e44ad', 'Cancelled': '#2c3e50'
    }
    for col in severity_season.columns:
        fig.add_trace(go.Bar(
            name=col, x=severity_season.index, y=severity_season[col],
            marker_color=severity_colors.get(col, '#95a5a6')
        ))
    fig.update_layout(barmode='stack', height=450, yaxis_title='Percentage (%)',
                      xaxis_title='Season')
    st.plotly_chart(fig, use_container_width=True)

    # Month x Hour heatmap
    st.subheader("Delay Heatmap: Month × Hour")
    heatmap = df_comp_filtered.pivot_table(
        values='dep_delay', index='hour', columns='month', aggfunc='mean'
    )
    heatmap.columns = MONTH_NAMES
    fig = px.imshow(heatmap, color_continuous_scale='RdYlGn_r', aspect='auto',
                    labels={'x': 'Month', 'y': 'Hour', 'color': 'Avg Delay (min)'})
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Winter vs Summer comparison
    st.subheader("Winter vs Summer Delay Comparison")
    winter = df_comp_filtered[df_comp_filtered['season'] == 'Winter']['dep_delay'].dropna()
    summer = df_comp_filtered[df_comp_filtered['season'] == 'Summer']['dep_delay'].dropna()

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("**Winter (Dec-Feb)**")
        st.markdown(f"- Mean delay: **{winter.mean():.1f} min**")
        st.markdown(f"- Median delay: **{winter.median():.1f} min**")
        st.markdown(f"- % delayed >15 min: **{(winter > 15).mean() * 100:.1f}%**")
        st.markdown(f"- Max delay: **{winter.max():.0f} min**")
    with col_r:
        st.markdown("**Summer (Jun-Aug)**")
        st.markdown(f"- Mean delay: **{summer.mean():.1f} min**")
        st.markdown(f"- Median delay: **{summer.median():.1f} min**")
        st.markdown(f"- % delayed >15 min: **{(summer > 15).mean() * 100:.1f}%**")
        st.markdown(f"- Max delay: **{summer.max():.0f} min**")

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=winter.clip(-60, 200), name='Winter',
                               marker_color='#3498db', opacity=0.6, nbinsx=60))
    fig.add_trace(go.Histogram(x=summer.clip(-60, 200), name='Summer',
                               marker_color='#e74c3c', opacity=0.6, nbinsx=60))
    fig.update_layout(barmode='overlay', height=400,
                      xaxis_title='Departure Delay (min)', yaxis_title='Count')
    st.plotly_chart(fig, use_container_width=True)


# ─── Footer ───
st.sidebar.markdown("---")
st.sidebar.caption("AirFly Insights | NYC Flights 2013 | Data Visualization Project")
