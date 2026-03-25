import pandas as pd
from sales_analyzer.analyzer import total_sales

def test_total():
    df = pd.DataFrame({"sales":[10,20,30]})
    assert total_sales(df) == 60
