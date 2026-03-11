import pandas as pd

def analyze_sales(df):
    """
    Perform sales analysis
    """

    results = {}

    # total sales
    results["total_sales"] = df["Sales"].sum()

    # average sales
    results["average_sales"] = df["Sales"].mean()

    # top products
    results["top_products"] = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

    # monthly sales
    df["Month"] = df["Date"].dt.month
    results["monthly_sales"] = df.groupby("Month")["Sales"].sum()

    return results
