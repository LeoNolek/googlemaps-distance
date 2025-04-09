import pandas as pd

def read_excel(file_path):
    try:
        # Read the Excel file
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None