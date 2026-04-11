from analytics import get_latest, daily_avg_temp, max_wind
import matplotlib.pyplot as plt
print(get_latest())
print(daily_avg_temp())
print(max_wind)


plt.bar('date', 'avg_temp', data =daily_avg_temp())
plt.show()