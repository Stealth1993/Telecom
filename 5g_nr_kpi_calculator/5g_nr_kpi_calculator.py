import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_5g_data(samples=1000):
    timestamps = pd.date_range(start="2023-01-01", periods=samples, freq="S")
    throughput = np.random.normal(100, 20, samples)  # Gbps
    latency = np.random.normal(10, 2, samples)     # ms
    jitter = np.random.uniform(0, 1, samples)      # ms
    return pd.DataFrame({"timestamp": timestamps, "throughput": throughput, "latency": latency, "jitter": jitter})

def calculate_kpis(data):
    return {
        "throughput": data["throughput"].mean(),
        "latency": data["latency"].mean(),
        "jitter": data["jitter"].mean()
    }

def plot_kpis(kpis):
    fig, ax = plt.subplots()
    ax.bar(kpis.keys(), kpis.values(), color=['blue', 'green', 'purple'])
    ax.set_title("5G NR KPIs")
    ax.set_ylabel("Value")
    plt.show()

def main():
    data = generate_5g_data()
    kpis = calculate_kpis(data)
    print("5G NR KPIs:")
    for kpi, value in kpis.items():
        print(f"Average {kpi.capitalize()}: {value:.2f}")
    plot_kpis(kpis)

if __name__ == "__main__":
    main()