import pandas as pd

dataset_1_path = 'Truth_dataset_path'
dataset_2_path = 'Predicted_file_path'

df1 = pd.read_csv(dataset_1_path)
df2 = pd.read_csv(dataset_2_path)

# Function to print full text and other columns for a given id from both datasets
def print_data_by_id(dataset1, dataset2, id_value):
    # String type id handling
    row1 = dataset1[dataset1['id'].astype(str) == str(id_value)]
    row2 = dataset2[dataset2['id'].astype(str) == str(id_value)]
    
    if not row1.empty:
        print(f"Data from Dataset 1 (ID {id_value}):")
        print(row1.to_string(index=False))
        print("\n")
    else:
        print(f"ID {id_value} not found in Dataset 1.\n")
    
    if not row2.empty:
        print(f"Data from Dataset 2 (ID {id_value}):")
        print(row2.to_string(index=False))
        print("\n")
    else:
        print(f"ID {id_value} not found in Dataset 2.\n")

id_input = input("Enter the ID: ")
print_data_by_id(df1, df2, id_input)
