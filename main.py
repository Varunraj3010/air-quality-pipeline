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

def main():
    data = fetch()
    df = pd.DataFrame(data["hourly"])
    print(df.head())

if __name__ == "__main__":
    main()
