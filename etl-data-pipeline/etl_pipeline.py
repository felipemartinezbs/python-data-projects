import requests
import pandas as pd
import matplotlib.pyplot as plt

print("Starting ETL pipeline...")

# EXTRACT
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

print("Data extracted from API")

# TRANSFORM
df = pd.DataFrame(data)

df = df[[
    "name",
    "symbol",
    "current_price",
    "market_cap",
    "total_volume"
]]

df = df.sort_values(by="market_cap", ascending=False)

print("Data transformed")

# LOAD
df.to_csv("crypto_market_dataset.csv", index=False)

print("Dataset saved")

# Visualization
top10 = df.head(10)

top10.plot(
    x="name",
    y="market_cap",
    kind="bar"
)

plt.title("Top 10 Crypto by Market Cap")
plt.ylabel("Market Cap")
plt.xlabel("Cryptocurrency")

plt.tight_layout()

plt.savefig("crypto_market_chart.png")

print("Chart generated")

print("ETL pipeline finished successfully")