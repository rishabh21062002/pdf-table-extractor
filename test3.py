import csv

# Define the CSV filename
csv_filename = "bank_statement.csv"

# Data extracted from your statement (Example)
data = [
    ["01-APR-2022", "B/F", "", "", "30,63,234.66Dr"],
    ["04-APR-2022", "T", "BY 06971000010040", "25,000.00", "30,38,234.66Dr"],
    ["04-APR-2022", "C", "By Cash", "40,000.00", "29,98,234.66Dr"],
    ["20-APR-2022", "T", "BY 06971000010040", "2,000.00", "29,96,234.66Dr"],
    ["29-APR-2022", "C", "By Cash", "35,000.00", "29,61,234.66Dr"],
    ["30-APR-2022", "T", "Int. Coll: 01-04-2022 to 30-04-2022", "26,168.00", "29,87,402.66Dr"],
    ["30-MAY-2022", "T", "Inspection Charges Yearly", "3,540.00", "29,90,942.66Dr"],
    ["31-MAY-2022", "T", "Int. Coll: 01-05-2022 to 31-05-2022", "26,897.00", "30,17,839.66Dr"],
    ["01-JUL-2022", "T", "Cr-IMPS :P2A/05CREDIT/IMPS/21821/9308141/jaiveer", "30,000.00", "30,14,175.66Dr"],
    ["02-JUL-2022", "T", "Cr-IMPS :P2A/TRAMO TECH/", "1.00", "30,14,174.66Dr"],
    ["02-JUL-2022", "T", "Cr-IMPS :P2A", "25,000.00", "29,89,174.66Dr"],
    ["25-JUL-2022", "C", "By Cash", "15,000.00", "29,64,292.66Dr"],
    ["28-JUL-2022", "C", "TO CASH PAID TO JAIDEEP PADDA", "20,000.00", "29,82,292.66Dr"],
    ["30-JUL-2022", "T", "Int. Coll: 01-07-2022 to 31-07-2022", "31,582.00", "30,03,874.66Dr"],
]

# Define CSV column headers
headers = ["Date", "Type", "Description", "Amount", "Balance"]

# Write to CSV file
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write headers
    writer.writerows(data)  # Write data rows

print(f"✅ CSV file '{csv_filename}' has been created successfully!")
