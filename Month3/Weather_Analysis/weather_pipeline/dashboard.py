import streamlit as st
import sqlite3
import pandas as pd
from analytics import daily_avg_temp
import matplotlib.pyplot as plt

st.title("Weather Dashboard")

# Load the data
conn = sqlite3.connect("weather.db")
df = pd.read_sql("select * from weather", conn)
if df.empty:
    st.warning("No data available")
else:
    df['time'] = pd.to_datetime(df['time'])
    st.subheader("Raw data")
    st.dataframe(df)

    st.subheader("Temperature Trend")
    st.line_chart(df.set_index("time")['temperature'])

    st.subheader("Humidity Trend")
    st.line_chart(df.set_index('time')['humidity'])

    st.subheader("Wind Speed")
    st.line_chart(df.set_index('time')['wind_speed'])

    st.subheader("Daily Average Temperature")

st.subheader("📊 Daily Average Temperature (Bar Chart)")

df_avg = daily_avg_temp()

if df_avg.empty:
    st.warning("No data available for bar chart")
else:
    df_avg["date"] = df_avg["date"].astype(str)

    fig, ax = plt.subplots()
    ax.bar(df_avg["date"], df_avg["avg_temp"])

    ax.set_xlabel("Date")
    ax.set_ylabel("Average Temperature")
    ax.set_title("Daily Average Temperature")

    plt.xticks(rotation=45)

    st.pyplot(fig)
conn.close