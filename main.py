import pandas as pd
from correlation import plot_correlation_heatmap
from modelling import regression_model 
from findMax import find_optimal_cell_density 
from sklearn.preprocessing import StandardScaler
from findMax2 import add_cell_density_and_save
from itertools import product

excel_file_path = 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\cleaned_data.xlsx'
df = pd.read_excel(excel_file_path)
plot_correlation_heatmap(df)

target_column = 'CellDensity'  
feature_columns = ['Temperature', 'Salinity','darkTime', 'lightTime','Day',  'LightIntensity','CM_npk','CM_map','CM_f2']

model = regression_model(df, feature_columns,target_column)

data = pd.read_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\new_data.xlsx')
feature_names = ['Temperature', 'Salinity','darkTime', 'lightTime','Day',  'LightIntensity','CM_npk','CM_map','CM_f2']
add_cell_density_and_save(model, feature_names, data, 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\new_data2.xlsx')
# Call the function to find the optimal cell density and feature values
max_cell_density, optimal_feature_values = find_optimal_cell_density(model, feature_names, data)

data = data.reset_index(drop=True)
print("Maximum Cell Density:", max_cell_density)
print("Optimal Feature Values:", optimal_feature_values)
