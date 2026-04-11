import sqlite3
import pandas as pd
DB_Path = 'weather.db'

#------------------
# Latest weather Data
#--------------------
def get_latest():
    conn = sqlite3.connect(DB_Path)

    query = """
    select * from weather
    ORDER BY time DESC
    Limit 1
    """
    df = pd.read_sql(query, conn)
    conn.close()

    return df

#-------------------------
# Daily Average Temperature
#-------------------------
def daily_avg_temp():
    conn =sqlite3.connect(DB_Path)

    query = """
    SELECT DATE(time) as date,
        AVG(temperature) as avg_temp
        from weather
        Group by DATE(time) order by date  
    """
    df= pd.read_sql(query, conn)
    conn.close()
    return df

#--------------------
# Maximum wind speed
#--------------------

def max_wind():
    conn = sqlite3.connect(DB_Path)

    query = """
    SELECT MAX(wind_speed) as max_wind from weather
    """
    df= pd.read_sql(query, conn)
    conn.close()

    return df

# -------------------------------
# 4. Custom Query (Flexible)
# -------------------------------
def run_query(query):
    conn = sqlite3.connect(DB_Path)

    df = pd.read_sql(query, conn)

    conn.close()

    return df
