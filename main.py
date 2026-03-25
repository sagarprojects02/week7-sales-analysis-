from sales_analyzer.data_loader import load_data
from sales_analyzer.data_cleaner import clean_data, save_processed
from sales_analyzer.analyzer import total_sales, average_sales
from sales_analyzer.visualizer import plot_sales
from sales_analyzer.reporter import generate_report, save_report

raw_path = "data/raw/sales_data.csv"
processed_path = "data/processed/cleaned_data.csv"
report_path = "data/reports/report.txt"

df = load_data(raw_path)

df = clean_data(df)

save_processed(df, processed_path)

total = total_sales(df)
avg = average_sales(df)

report = generate_report(total, avg)

save_report(report, report_path)

print(report)

plot_sales(df)
