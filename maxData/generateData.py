import pandas as pd
from itertools import product

Temperature= [24,26, 28, 30,32]
Salinity = [30, 32, 34, 36]
darkTime = [14, 18,20,24]
lightTime = [4, 6,10]
Day= [1, 2, 3,4, 5, 6,7,8]
LightIntensity = [300,400,500, 600,700]
CM_f2 = [1,0]
CM_map = [1,0]
CM_npk = [1,0]

# Create a list of feature value ranges
feature_values = [Temperature, Salinity,darkTime, lightTime,Day, LightIntensity,CM_npk,CM_map,CM_f2] 


# Define the feature names
feature_names = ['Temperature', 'Salinity','darkTime', 'lightTime','Day',  'LightIntensity','CM_npk','CM_map','CM_f2'] 


combinations = list(product(Temperature,Salinity, darkTime, lightTime, Day, LightIntensity , CM_npk,CM_map,CM_f2))
# Create a DataFrame with all combinations
new_data = pd.DataFrame(combinations, columns=['Temperature', 'Salinity','darkTime', 'lightTime','Day',  'LightIntensity','CM_npk','CM_map','CM_f2'] )
new_data = new_data[~((new_data['CM_f2'] == 1) & (new_data['CM_map'] == 1) & (new_data['CM_npk'] == 1))]
new_data = new_data[~((new_data['CM_f2'] == 1) & (new_data['CM_map'] == 1) & (new_data['CM_npk'] == 0))]
new_data = new_data[~((new_data['CM_f2'] == 0) & (new_data['CM_map'] == 1) & (new_data['CM_npk'] == 1))]
new_data = new_data[~((new_data['CM_f2'] == 1) & (new_data['CM_map'] == 0) & (new_data['CM_npk'] == 1))]
new_data= new_data[~((new_data['CM_f2'] == 0) & (new_data['CM_map'] == 0) & (new_data['CM_npk'] == 0))]

new_data.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\new_data.xlsx', index=False, engine='xlsxwriter')