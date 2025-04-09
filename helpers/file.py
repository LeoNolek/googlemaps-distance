import pandas as pd

def read_excel(file_path):
    try:
        # Read the Excel file
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None
    
def find_value_in_excel(file_path, value):
    data = read_excel(file_path)
    if data is not None:
        for row_idx, row in data.iterrows():
            for col_idx, cell in enumerate(row):
                if cell == value:
                    return row_idx, col_idx
    return None

def iterate_column_values(file_path, column_idx):
    data = read_excel(file_path)
    if data is not None:
        if 0 <= column_idx < len(data.columns):
            for value in data.iloc[:, column_idx]:
                yield value
        else:
            print(f"Column index {column_idx} is out of range.")