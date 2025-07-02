import requests
import smtplib
import time
from email.mime.text import MIMEText

def fetch_kpis(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data["throughput"], data["latency"]
    except Exception as e:
        print(f"Error fetching KPIs: {e}")
        return None, None

def send_alert(throughput, latency):
    msg = MIMEText(f"Alert: Throughput={throughput:.2f} Mbps, Latency={latency:.2f} ms")
    msg["Subject"] = "KPI Threshold Exceeded"
    msg["From"] = "monitor@example.com"
    msg["To"] = "admin@example.com"
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.login("username", "password")
        server.send_message(msg)

def monitor_kpis():
    url = "http://kpi-dashboard.local/api/kpis"
    while True:
        throughput, latency = fetch_kpis(url)
        if throughput and (throughput < 50 or latency > 30):
            send_alert(throughput, latency)
        time.sleep(3600)

def main():
    print("Starting KPI monitoring...")
    monitor_kpis()

if __name__ == "__main__":
    main()