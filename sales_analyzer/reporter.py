import pandas as pd

def generate_report(results):
    """
    Generate sales report
    """

    report = {
        "Total Sales": results["total_sales"],
        "Average Sales": results["average_sales"]
    }

    report_df = pd.DataFrame(list(report.items()), columns=["Metric", "Value"])

    report_df.to_csv("data/reports/sales_summary.csv", index=False)

    # save top products
    results["top_products"].to_csv("data/reports/top_products.csv")

    # save monthly sales
    results["monthly_sales"].to_csv("data/reports/monthly_sales.csv")

    print("Report generated successfully")
