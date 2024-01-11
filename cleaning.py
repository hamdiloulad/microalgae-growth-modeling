import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\data.xlsx'
df = pd.read_excel(excel_file_path)

features = df.drop(columns=['CellDensity'])
# Iterate through each feature and print unique values
for column in features.columns:
    unique_values = features[column].unique()
    print(f"Unique values for feature '{column}': {unique_values}")

df['CM'] = df['CM'].replace("F2 de guillard", "f2")
df['CM'] = df['CM'].replace("monoamonium phosphate", "map")


num_rows = df.shape[0]
print(f"Number of Rows: {num_rows}")
# Print the name of each feature and the number of null values in it
print("Feature Name\t\tNumber of Null Values")
for column in df.columns:
    null_count = df[column].isnull().sum()
    print(f"{column}\t\t\t{null_count}")

# Remove rows with null values in the 'temperature' column
df_complete = df.dropna(subset=['Temperature', 'Salinity', 'Day','LightIntensity','CM'])

# Verify that the null values in the 'temperature' column have been removed
print("\nAfter removing null values")
for column in df_complete.columns:
    null_count = df_complete[column].isnull().sum()
    print(f"{column}\t\t\t{null_count}")
num_rows = df_complete.shape[0]
print(f"Number of Rows: {num_rows}")