"""
generate_ecommerce.py
Generates a reproducible synthetic e-commerce transaction dataset for Project 03.
Seed is fixed at 42 for 100% reproducibility.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

NUM_TRANSACTIONS = 2500
NUM_CUSTOMERS = 350

# Customer IDs with a Pareto power-law distribution
# Some customers buy frequently, most buy occasionally
customer_pool = [f"CUST-{1000 + i}" for i in range(1, NUM_CUSTOMERS + 1)]
customer_weights = np.random.pareto(a=1.8, size=NUM_CUSTOMERS)
customer_weights /= customer_weights.sum()

customers = np.random.choice(customer_pool, size=NUM_TRANSACTIONS, p=customer_weights)

# Date distribution spanning 2023 with Q4 seasonality (holidays)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
total_days = (end_date - start_date).days

# Month weights: higher in Nov (month 11) and Dec (month 12)
dates = []
for _ in range(NUM_TRANSACTIONS):
    # Random day with higher probability in late months
    day_offset = int(np.random.beta(a=2.0, b=1.5) * total_days)
    dates.append(start_date + timedelta(days=day_offset))

dates.sort()

categories_info = {
    "Electronics": {"price_range": (120, 950), "weight": 0.22},
    "Fashion & Apparel": {"price_range": (25, 160), "weight": 0.28},
    "Home & Kitchen": {"price_range": (35, 240), "weight": 0.20},
    "Beauty & Personal Care": {"price_range": (15, 85), "weight": 0.14},
    "Sports & Outdoors": {"price_range": (25, 280), "weight": 0.10},
    "Books & Stationery": {"price_range": (10, 45), "weight": 0.06}
}

category_names = list(categories_info.keys())
category_weights = [categories_info[c]["weight"] for c in category_names]

chosen_categories = np.random.choice(category_names, size=NUM_TRANSACTIONS, p=category_weights)

quantities = []
unit_prices = []
total_amounts = []
payment_methods = []
statuses = []

payment_pool = ["Credit Card", "UPI", "Debit Card", "Net Banking", "Cash on Delivery"]
payment_weights = [0.38, 0.32, 0.14, 0.10, 0.06]

status_pool = ["Completed", "Returned", "Cancelled"]
status_weights = [0.89, 0.07, 0.04]

for i in range(NUM_TRANSACTIONS):
    cat = chosen_categories[i]
    min_p, max_p = categories_info[cat]["price_range"]
    price = round(np.random.uniform(min_p, max_p), 2)
    qty = int(np.random.choice([1, 2, 3, 4, 5], p=[0.55, 0.25, 0.12, 0.05, 0.03]))
    
    unit_prices.append(price)
    quantities.append(qty)
    total_amounts.append(round(price * qty, 2))
    payment_methods.append(np.random.choice(payment_pool, p=payment_weights))
    statuses.append(np.random.choice(status_pool, p=status_weights))

order_ids = [f"ORD-{20230001 + i}" for i in range(NUM_TRANSACTIONS)]

df = pd.DataFrame({
    "Order_ID": order_ids,
    "Date": [d.strftime("%Y-%m-%d") for d in dates],
    "Customer_ID": customers,
    "Product_Category": chosen_categories,
    "Quantity": quantities,
    "Unit_Price": unit_prices,
    "Total_Amount": total_amounts,
    "Payment_Method": payment_methods,
    "Status": statuses
})

output_path = "DataSphereAI/data/ecommerce_data.csv"
df.to_csv(output_path, index=False)
print(f"Generated {len(df)} transactions in {output_path}")
print(df.head())
print("\nKPI Summary (Completed Orders):")
completed = df[df["Status"] == "Completed"]
print(f"Total Revenue: ${completed['Total_Amount'].sum():,.2f}")
print(f"Total Completed Transactions: {len(completed)}")
print(f"Unique Customers: {completed['Customer_ID'].nunique()}")
print(f"Average Order Value: ${completed['Total_Amount'].mean():.2f}")
