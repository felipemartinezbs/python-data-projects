import pandas as pd
import matplotlib.pyplot as plt

print("Starting data analysis project...")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

print("\nDataset loaded")
print(df.head())

# análisis

avg_tip = df["tip"].mean()

print("\nAverage tip:", avg_tip)

tips_by_day = df.groupby("day")["tip"].mean()

print("\nAverage tip by day:")
print(tips_by_day)

# gráfico

tips_by_day.plot(kind="bar")

plt.title("Average Tip by Day")
plt.ylabel("Tip")
plt.xlabel("Day")

plt.tight_layout()

plt.savefig("tips_analysis_chart.png")

print("\nChart saved")