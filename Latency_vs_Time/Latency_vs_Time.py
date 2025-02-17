import pandas as pd
import matplotlib.pyplot as plt

#loading data
df = pd.read_csv('network_data.csv')
print(df.head())

#filter_data

filtered_data = df[df['Latency'] < 0.1]
print(filtered_data.head())

#plotting data

plt.figure(figsize=(10,6))
plt.plot(filtered_data['Time'], filtered_data['Latency'], marker='o', color='r', linestyle='-')
plt.xlabel('Time(s)')
plt.ylabel('Latency(ms)')
plt.title('Latency vs Time')
plt.grid()
plt.show()