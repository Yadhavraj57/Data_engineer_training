import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

df['revenue'] = df['quantity'] * df['sale_price']
df['cost_total'] = df['quantity'] * df['cost']
df['profit'] = df['revenue'] - df['cost_total']
df['discount_amount'] = df['sale_price'] * df['discount_pct'] / 100

df = df.dropna()

df['sale_date'] = pd.to_datetime(df['sale_date'])

store_summary = df.groupby('store_id')[['revenue', 'profit']].sum().reset_index()

product_summary = df.groupby('product_id')[['revenue', 'profit']].sum().reset_index()

print("Store Summary")
print(store_summary)

print("\nProduct Summary")
print(product_summary)

store_summary.to_csv("store_summary.csv", index=False)
product_summary.to_csv("product_summary.csv", index=False)