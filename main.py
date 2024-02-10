import pandas as pd
from correlation import plot_correlation_heatmap
from modelling import regression_model 
from findMax import find_optimal_cell_density 


excel_file_path = 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\cleaned_data.xlsx'
df = pd.read_excel(excel_file_path)
plot_correlation_heatmap(df)

target_column = 'CellDensity'  
feature_columns = ['Temperature', 'LightIntensity','Salinity','Day', 'lightTime','darkTime','CM_f2','CM_map','CM_npk']  

model = regression_model(df, feature_columns,target_column)

Temperature= [24,26, 28, 30,32]
LightIntensity = [300,400,500, 600,700]
darkTime = [14, 18,20,24]
lightTime = [4, 6,10]
Day= [1, 2, 3,4, 5, 6,7,8]
Salinity = [30, 32, 34, 36]
CM_f2 = [True,False]
CM_map = [True,False]
CM_npk = [True,False]

# Create a list of feature value ranges
feature_values = [Temperature, LightIntensity,Salinity,Day,lightTime,darkTime,CM_f2,CM_map,CM_npk]


# Define the feature names
feature_names = ['Temperature', 'LightIntensity','Salinity','Day', 'lightTime','darkTime','CM_f2','CM_map','CM_npk'] 

# Call the function to find the optimal cell density and feature values
max_cell_density, optimal_feature_values = find_optimal_cell_density(model, feature_names, *feature_values)

# Print the results
print("Maximum Cell Density:", max_cell_density)
print("Optimal Feature Values:", optimal_feature_values)
