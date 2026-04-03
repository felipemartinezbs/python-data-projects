import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Extrayendo datos de películas...")

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

df = pd.DataFrame({
    "title": titles,
    "price": prices
})

print(df)

df.to_csv("books_dataset.csv", index=False)

print("\nDataset guardado correctamente.")