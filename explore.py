import pandas as pd
import requests

url = "https://air-quality-api.open-meteo.com/v1/air-quality"

# Pass hourly variables as a list or a clean comma-separated string without spaces
params = {
    "latitude": 19.07,
    "longitude": 72.88,
    "hourly": ["pm10", "pm2_5"],  # Passing a list lets requests handle formatting
    "past_days": 7,
    "forecast_days": 1,
}

response = requests.get(url, params=params, timeout=30)

print(f"Status Code: {response.status_code}")

if response.status_code != 200:
    # Print Open-Meteo's exact error response to diagnose instantly
    print("API Error Response:", response.json())
else:
    data = response.json()
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])

    print("\nDataFrame Head:")
    print(df.head())
    print("\nDataFrame Tail:")
    print(df.tail())
    print("\nDataFrame Summary:")
    print(df.info())
    print("\nDataFrame Statistics:")
    print(df.describe())