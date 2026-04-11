import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("weather.db")

df = pd.read_sql("SELECT * FROM weather", conn)

print(df)

df['temperature'].plot(kind = 'line')
plt.show()
