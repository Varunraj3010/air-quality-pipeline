import matplotlib.pyplot as plt
import pandas as pd
from db import get_connection

def main():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT time, pm2_5 FROM readings ORDER BY time")
        rows = cur.fetchall()
    conn.close()

    # Convert database rows into a Pandas DataFrame
    df = pd.DataFrame(rows, columns=["time", "pm2_5"])

    # Generate the plot
    plt.figure(figsize=(10, 4))
    plt.plot(df["time"], df["pm2_5"], color="tab:red", linewidth=1.5)
    plt.title("PM2.5 in Mumbai, Last 7 Days")
    plt.ylabel("µg/m³")
    plt.xlabel("Time")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Save the chart as an image
    plt.savefig("pm25_trend.png")
    print("Chart generated and saved successfully as pm25_trend.png!")

if __name__ == "__main__":
    main()