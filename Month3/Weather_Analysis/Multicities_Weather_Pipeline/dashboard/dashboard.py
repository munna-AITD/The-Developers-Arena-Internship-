import streamlit as st
import pandas as pd
import sqlite3
from streamlit_autorefresh import st_autorefresh

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Weather Analytics Dashboard", layout="wide")

st.title("Multi-City Weather Analytics Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
conn = sqlite3.connect("data/weather_data.db")

query = """
SELECT 
    c.city_name,
    w.temperature_c,
    w.humidity,
    w.pressure_hpa,
    w.wind_speed_mps,
    w.weather_condition,
    w.timestamp
FROM weather_data w
JOIN cities c ON w.city_id = c.city_id
"""

df = pd.read_sql(query, conn)
conn.close()

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

cities = df['city_name'].unique()
selected_cities = st.sidebar.multiselect("Select Cities", cities, default=cities)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['timestamp'].min(), df['timestamp'].max()]
)

# Apply filters
filtered_df = df[
    (df['city_name'].isin(selected_cities)) &
    (df['timestamp'].dt.date >= date_range[0]) &
    (df['timestamp'].dt.date <= date_range[1])
]

# -----------------------------
# KPI SECTION
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("🌡 Avg Temperature", f"{filtered_df['temperature_c'].mean():.2f} °C")
col2.metric("💧 Avg Humidity", f"{filtered_df['humidity'].mean():.2f} %")
col3.metric("🌬 Avg Wind Speed", f"{filtered_df['wind_speed_mps'].mean():.2f} m/s")

# -----------------------------
# HIGHEST TEMP CITY
# -----------------------------
st.subheader("🏆 Hottest City")

hottest_city = (
    filtered_df.groupby("city_name")["temperature_c"]
    .mean()
    .idxmax()
)

st.success(f"Hottest City: {hottest_city}")

# -----------------------------
# TEMPERATURE TREND
# -----------------------------
st.subheader("📈 Temperature Trend (Last 30 Days)")

last_30 = filtered_df[
    filtered_df['timestamp'] >= pd.Timestamp.now() - pd.Timedelta(days=30)
]

trend = last_30.groupby(
    [last_30['timestamp'].dt.date, 'city_name']
)["temperature_c"].mean().unstack()

st.line_chart(trend)

# -----------------------------
# PEAK TEMPERATURE HOURS
# -----------------------------
st.subheader("Peak Temperature Hours")

filtered_df['hour'] = filtered_df['timestamp'].dt.hour

peak = filtered_df.groupby(
    ['hour', 'city_name']
)["temperature_c"].mean().unstack()

st.line_chart(peak)

# -----------------------------
# SEASON ANALYSIS
# -----------------------------
st.subheader("Seasonal Analysis")

def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Summer"
    elif month in [6,7,8]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

filtered_df['season'] = filtered_df['timestamp'].dt.month.apply(get_season)

season_data = filtered_df.groupby("season")["temperature_c"].agg(["max", "min"])

st.dataframe(season_data)

# -----------------------------
# HUMIDITY DISTRIBUTION
# -----------------------------
st.subheader(" Humidity Distribution")

st.bar_chart(filtered_df.groupby("city_name")["humidity"].mean())

# -----------------------------
# RAW DATA
# -----------------------------
st.subheader(" Raw Data")

st.dataframe(filtered_df)

# SIDEBAR FILTERS
st.sidebar.header("🔍 Filters")

cities = df['city_name'].unique()

selected_city = st.sidebar.selectbox("Select City", cities)

filtered_df = df[df['city_name'] == selected_city]

st.subheader(" Raw Data")
st.dataframe(filtered_df)

# DOWNLOAD BUTTON
st.download_button(
    label=" Download Data",
    data=filtered_df.to_csv(index=False),
    file_name="weather_data.csv",
    mime="text/csv"
)
st.subheader(" Alerts")

if filtered_df['temperature_c'].max() > 40:
    st.error(" Heat Alert! Temperature above 40°C")

if filtered_df['temperature_c'].min() < 5:
    st.warning(" Cold Alert! Temperature below 5°C")

import time

# Auto refresh every 60 seconds
time.sleep(60)
st_autorefresh(interval=60000, key="refresh")