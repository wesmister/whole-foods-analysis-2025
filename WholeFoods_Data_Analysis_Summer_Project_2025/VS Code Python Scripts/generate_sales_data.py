import pandas as pd
import random
from datetime import datetime, timedelta

# Define departments and products with unit prices
departments = {
    "Bakery": {
        "Croissants": 2.50,
        "Whole Wheat Boules": 4.50,
        "Chocolate Chip Cookies": 1.75,
        "Blueberry Muffins": 2.25,
        "Apple Pies": 7.99,
    },
    "Meat & Seafood": {
        "Ground Beef": 6.99,
        "Whole Chickens": 9.50,
        "Sirloin Steaks": 14.99,
        "Frozen Lobster Tails": 19.99,
        "Salmon": 12.99,
    },
    "Produce": {
        "Bananas": 0.59,
        "Organic Avocados": 1.49,
        "Baby Spinach": 3.29,
        "Strawberries": 4.49,
        "Bell Peppers": 1.29,
    },
    "Dairy": {
        "Organic Whole Milk": 5.99,
        "Greek Yogurt": 1.29,
        "Cheddar Cheese": 3.99,
        "Cage-Free Eggs": 4.49,
        "Almond Milk": 3.79,
    },
    "Grocery": {
        "Bottled Water (12-pack)": 4.99,
        "Pasta Sauce": 3.49,
        "Organic Peanut Butter": 5.49,
        "Olive Oil": 9.99,
        "Canned Black Beans": 1.19,
    },
}

# Create list of dates for June 2025
start_date = datetime(2025, 6, 1)
end_date = datetime(2025, 6, 30)
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Generate data
data = []

for date in dates:
    for dept, products in departments.items():
        for product, price in products.items():
            units_sold = random.randint(10, 200)
            total_sales = round(units_sold * price, 2)
            data.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Department": dept,
                "Product": product,
                "Unit Price ($)": price,
                "Units Sold": units_sold,
                "Total Sales ($)": total_sales
            })

# Create DataFrame and export to Excel
df = pd.DataFrame(data)
df.to_excel("WholeFoods_Sales_June2025.xlsx", index=False)

print("✅ File created: WholeFoods_Sales_June2025.xlsx")
