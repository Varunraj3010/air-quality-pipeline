import requests
import pandas as pd

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
    df = df.dropna(subset=["pm10", "pm2_5"], how = "all")  # Remove rows with missing values
    df = df[(df["pm10"].isna() | (df["pm10"] >=0)) & (df["pm2_5"].isna() | (df["pm2_5"] >= 0))]  # Filter out negative values
    return df

def main():
    data = fetch()
    df = pd.DataFrame(data["hourly"])
    print(len(df))
    df = clean(data)
    print(len(df))
    print(df.head())

if __name__ == "__main__":
    main()