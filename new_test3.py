import pandas as pd
import re

def extract_tables_from_text(file_path, output_excel):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # headers = ["Date", "Type", "Description", "Amount", "Balance"]
    tables = []
    current_table = []
    table_start=False
    same_row_add =False
    
    for line in lines:
        
        line = line.strip()

        if not line or "<<<" in line:
            continue

        if re.search(r"BANK NAME",line):
            same_row_add=False
            table_start=False

            if current_table:
                tables.append(pd.DataFrame(current_table))  # Save the last table before starting new one
            current_table = [] 
            continue

        # Detect a new statement line
        if re.search(r"\s*Statement of account for the period", line, re.IGNORECASE):
            
            same_row_add=False
            table_start=True
            
            continue
        if table_start:
            parts = re.split(r'\s{2,}', line)
            if same_row_add:
                current_table[-1].extend(parts)
                same_row_add=False
            else:
                match = re.match(r"(\d{2}-[A-Za-z]{3}\s*-\s*\d{4})\s+(\S+)\s+(.+)", line, re.IGNORECASE) 
                if match:
                    current_table.append(list(match.groups()))
                    same_row_add=True
   
    # Save last table
    if current_table:
        tables.append(pd.DataFrame(current_table))

    # Save to Excel
    with pd.ExcelWriter(output_excel) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)

# Example usage

