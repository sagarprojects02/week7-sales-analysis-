def generate_report(total, avg):
    report = f"""
SALES REPORT
Total Sales: {total}
Average Sales: {avg}
"""
    return report


def save_report(text, path):
    with open(path, "w") as f:
        f.write(text)
