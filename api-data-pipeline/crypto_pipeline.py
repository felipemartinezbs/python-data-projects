import requests
import pandas as pd

print("Descargando datos de criptomonedas...")

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

df = df[["name", "symbol", "current_price", "market_cap", "total_volume"]]

print("\nTop 10 criptomonedas:")
print(df)

df.to_csv("crypto_data.csv", index=False)

print("\nDataset guardado como crypto_data.csv")