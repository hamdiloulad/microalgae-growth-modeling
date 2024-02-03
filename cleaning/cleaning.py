import pandas as pd
from encoding import encode_and_save
from splitPhotoperiod import split_photoperiod
from scaling import scaling_and_save
from knnImputing import TuningKnnImputing
from sklearn.impute import KNNImputer
from sklearn.metrics import mean_squared_error
import numpy as np

# Path to the Excel file containing the data
excel_file_path = 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\data.xlsx'

# Read the data from the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

### print unique value
# Extract features by dropping the 'CellDensity' column
features = df.drop(columns=['CellDensity'])
# Iterate through each feature and print unique values
for column in features.columns:
    unique_values = features[column].unique()
    print(f"Unique values for feature '{column}': {unique_values}")

### Replace uncorrect values
df['CM'] = df['CM'].replace("F2 de guillard", "f2")
df['CM'] = df['CM'].replace("monoamonium phosphate", "map")
### Handling missing value
# Display the total number of rows in the DataFrame
num_rows = df.shape[0]
print(f"Number of Rows: {num_rows}")

# Print the name of each feature and the number of null values in it
print("Feature Name\t\tNumber of Null Values")
for column in df.columns:
    null_count = df[column].isnull().sum()
    print(f"{column}\t\t\t{null_count}")

# Remove rows with null values in specific columns
df_complete = df.dropna(subset=['Temperature', 'Salinity', 'Day', 'LightIntensity', 'CM'])
df_complete.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\complet_data.xlsx', index=False)
# Verify that the null values in the specified columns have been removed
print("\nAfter removing null values")
for column in df_complete.columns:
    null_count = df_complete[column].isnull().sum()
    print(f"{column}\t\t\t{null_count}")

# Split the photoperiod column into two separate columns
df_complete = split_photoperiod(df_complete)

# encoding 
df_encoded = encode_and_save(df_complete,['CM'])
# scaling
# List of numerical features for scaling
numerical_features = ['Temperature', 'Salinity', 'darkTime', 'lightTime', 'Day', 'LightIntensity', 'CellDensity']
df_scaled=scaling_and_save(df_encoded,numerical_features)

### knn imputaion
all_features = ['Temperature', 'Salinity', 'darkTime', 'lightTime', 'Day', 'LightIntensity', 'CellDensity', 'CM_npk', 'CM_map', 'CM_f2']
"""
result_rmse = TuningKnnImputing(df_scaled, all_features, 10, 'nan_euclidean', 'distance')
print(f"Root Mean Squared Error (RMSE) between true and imputed values: {result_rmse}")
"""

imputer_all = KNNImputer(n_neighbors=10, metric='nan_euclidean', weights='distance')
df_imputation_values = imputer_all.fit_transform(df_scaled[all_features])
df_imputation = pd.DataFrame(df_imputation_values, columns=all_features)
df_imputation.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\cleaned_data.xlsx', index=False)

