import pandas as pd
import re

def extract_transactions(file_path):
    """Extract transactions from the given text file and structure them into a table."""
    transactions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_transaction = {}
    
    for line in lines:
        line = line.strip()
        
        # Updated regex to capture "Transaction Details" before "Transaction Type"
        match = re.match(r'(\d{2}\.\w{3}\.\d{4})\s+(\d{2}\.\w{3}\.\d{4})\s+(\S+)\s+(\S+)\s+(\d+)\s+([CD])\s+([\d,]+\.\d{2})\s+(.+)\s+(\S+)$', line)
        if match:
            if current_transaction:  # Save previous transaction before starting a new one
                transactions.append(current_transaction)
            
            # Extract values from regex groups
            current_transaction = {
                "Transaction Date": match.group(1),
                "Value Date": match.group(2),
                "Transaction Reference": match.group(3),
                "Customer Reference": match.group(4),
                "Branch Number": match.group(5),
                "Credit/Debit": match.group(6),
                "Transaction Amount": match.group(7),
                "Transaction Details": match.group(8),  # Now capturing details before Transaction Type
                "Transaction Type": match.group(9),  # Last column
            }
        else:
            # Append additional details to the transaction description
            if current_transaction:
                current_transaction["Transaction Details"] += " " + line

    if current_transaction:
        transactions.append(current_transaction)

    return transactions

def save_to_csv(transactions, output_file):
    """Save the structured transactions into a CSV file."""
    df = pd.DataFrame(transactions)
    df.to_csv(output_file, index=False)
    print(f"Data successfully saved to {output_file}")

# File paths


# Process file and save output
def extract_structured_table(input_file,output_file):
    transactions = extract_transactions(input_file)
    save_to_csv(transactions, output_file)

print("✅ CSV file is ready!")
