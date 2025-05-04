import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

url = "https://www.ikea.com/us/en/cat/home-decor-products"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="product")
for product in products:
    name = product.find("h2").text if product.find("h2") else "No name"
    price = product.find("span", class_="price").text if product.find("span", class_="price") else "No price"
    print(f"{name}: {price}")

reviews = [
    "Love this product!",
    "Too expensive.",
    "Perfect for my decor."
]

print("\nSentiment Analysis:")
for review in reviews:
    sentiment = TextBlob(review).sentiment.polarity
    print(f"Review: {review} | Sentiment: {sentiment:.2f}")

sales_data = {"Month": ["Jan", "Feb", "Mar", "Apr"], "Sales": [1000, 1200, 1500, 1700]}
df_sales = pd.DataFrame(sales_data)

plt.figure(figsize=(8, 5))
plt.plot(df_sales["Month"], df_sales["Sales"], marker="o", linestyle="-", color='blue')
plt.title("Sales Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

categories = ["Eco-friendly", "Minimalist", "Handmade", "Smart Home", "Luxury"]
demand = [85, 70, 90, 60, 50]
df_demand = pd.DataFrame({"Category": categories, "Demand": demand})

plt.figure(figsize=(8, 5))
sns.barplot(data=df_demand, x="Category", y="Demand", hue="Category", palette="coolwarm", legend=False)
plt.title("Market Demand for Different Home Decor Categories")
plt.xlabel("Category")
plt.ylabel("Popularity Score")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

competitor_data = {
    "IKEA": np.random.randint(10, 150, 20),
    "West Elm": np.random.randint(50, 300, 20),
    "Etsy Sellers": np.random.randint(20, 200, 20)
}
df_competitors = pd.DataFrame(competitor_data)

plt.figure(figsize=(8, 5))
sns.boxplot(data=df_competitors)
plt.title("Competitor Price Range Distribution")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.show()

months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
sales_extended = [5000, 7000, 8500, 12000, 15000, 17000]

plt.figure(figsize=(8, 5))
plt.plot(months, sales_extended, marker="o", linestyle="-", color="b", linewidth=2)
plt.title("Home Decor Sales Trend Over 6 Months")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.show()

labels = ["Positive", "Neutral", "Negative"]
sizes = [65, 20, 15]  # Percentage distribution
colors = ["#2ecc71", "#f1c40f", "#e74c3c"]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
plt.title("Customer Sentiment Analysis on Home Decor Products")
plt.tight_layout()
plt.show()

followers = [1000, 5000, 10000, 25000, 50000, 100000]
sales = [2000, 7000, 12000, 20000, 35000, 50000]

plt.figure(figsize=(8, 5))
plt.scatter(followers, sales, color="purple", alpha=0.7)
plt.title("Impact of Instagram Followers on Sales")
plt.xlabel("Instagram Followers")
plt.ylabel("Sales ($)")
plt.xscale("log")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()