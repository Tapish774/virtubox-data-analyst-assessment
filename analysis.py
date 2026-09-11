"""
VirtuBox Data Analyst Assessment Pipeline
Candidate: Tapish Kumar
Dataset: Olist Brazilian E-Commerce
"""

import numpy as np
import pandas as pd

# 1. Load Data (Assumes datasets are downloaded locally or via Kaggle API)
print("Processing data...")
try:
    orders = pd.read_csv("olist_orders_dataset.csv")
    items = pd.read_csv("olist_order_items_dataset.csv")
    reviews = pd.read_csv("olist_order_reviews_dataset.csv")
    customers = pd.read_csv("olist_customers_dataset.csv")
    products = pd.read_csv("olist_products_dataset.csv")

    # 2. Parse Datetime Fields
    date_cols = [
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col])

    # 3. Clean and Calculate Metrics
    orders_clean = orders[
        (orders["order_status"] == "delivered")
        & (orders["order_delivered_customer_date"].notna())
    ].copy()
    orders_clean["delivery_days"] = (
        orders_clean["order_delivered_customer_date"]
        - orders_clean["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400
    orders_clean["delay_days"] = (
        orders_clean["order_delivered_customer_date"]
        - orders_clean["order_estimated_delivery_date"]
    ).dt.total_seconds() / 86400
    orders_clean["is_delayed"] = (orders_clean["delay_days"] > 0).astype(int)

    # Deduplicate reviews
    reviews_clean = (
        reviews.sort_values("review_creation_date")
        .groupby("order_id")
        .last()
        .reset_index()
    )

    # 4. Merge Master Table
    df = orders_clean.merge(items, on="order_id", how="inner")
    df = df.merge(
        reviews_clean[["order_id", "review_score"]], on="order_id", how="left"
    )
    df = df.merge(
        customers[["customer_id", "customer_unique_id", "customer_state"]],
        on="customer_id",
        how="inner",
    )
    df = df.merge(
        products[["product_id", "product_category_name"]],
        on="product_id",
        how="left",
    )
    df["product_category_name"] = df["product_category_name"].fillna("other")

    # Save output
    df.to_csv("processed_data.csv", index=False)
    print("Cleaned data successfully written to processed_data.csv")

    # Display Metrics
    print("\n--- Summary Statistics ---")
    print(
        "On-time vs Delayed CSAT:\n",
        df.groupby("is_delayed")["review_score"].mean(),
    )
    unique_custs = df.groupby("customer_unique_id")["order_id"].nunique()
    repeat_rate = (unique_custs > 1).sum() / len(unique_custs) * 100
    print(f"Repeat Purchase Rate: {repeat_rate:.2f}%")
except FileNotFoundError:
    print(
        "Source CSV files not found in current directory. Download from Kaggle to run locally."
    )
