import matplotlib.pyplot as plt

def create_charts(results):
    """
    Create charts from analysis results
    """

    # Monthly Sales Line Chart
    results["monthly_sales"].plot(kind="line")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.savefig("data/reports/monthly_sales.png")
    plt.close()

    # Top Products Bar Chart
    results["top_products"].head(5).plot(kind="bar")
    plt.title("Top Products")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.savefig("data/reports/top_products.png")
    plt.close()

    print("Charts created successfully")
