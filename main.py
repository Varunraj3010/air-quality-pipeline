import requests
import pandas as pd
import psycopg2
from db import get_connection, create_table, save

API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
LATITUDE = 19.07
LONGITUDE = 72.88

def fetch():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": "pm10,pm2_5",
        "past_days": 7,
        "forecast_days": 1,
    }
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def clean(data):
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    df = df.dropna(subset=["pm10", "pm2_5"], how="all")  # Remove rows with missing values
    df = df[(df["pm10"].isna() | (df["pm10"] >= 0)) & (df["pm2_5"].isna() | (df["pm2_5"] >= 0))]  # Filter out negative values
    return df

def main():
    try:
        data = fetch()
    except requests.RequestException as e:
        print(f"Could not fetch data: {e}")
        return

    df = clean(data)
    print(f"{len(df)} clean rows")
    
    try:
        conn = get_connection()
    except psycopg2.OperationalError as e:
        print(f"Database connection failed: {e}")
        return

    try:
        create_table(conn)
        inserted = save(conn, df)
        print(f"Inserted {inserted} new rows")
    finally:
        conn.close()

if __name__ == "__main__":
    main()