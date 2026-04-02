import pandas as pd

# Load dataset
data = pd.read_csv("Superstore.csv" , encoding='latin1')

# Show first 5 rows
print(data.head())

# Basic info
print(data.info())

# Check missing values
print(data.isnull().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Check again
print("After cleaning:")
print(data.isnull().sum())



# Total Sales
print("Total Sales:", data["Sales"].sum())

# Average Profit
print("Average Profit:", data["Profit"].mean())

# Sales by Region
print("\nSales by Region:")
print(data.groupby("Region")["Sales"].sum())

# Profit by Category
print("\nProfit by Category:")
print(data.groupby("Category")["Profit"].sum())

# Top 5 Products
print("\nTop Products:")
print(data.sort_values("Sales", ascending=False).head(5))

import matplotlib.pyplot as plt

data.groupby("Region")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()