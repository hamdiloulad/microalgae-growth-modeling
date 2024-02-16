import numpy as np
import pandas as pd

def add_cell_density_and_save(model, feature_names, data, output_excel_path):
    # Add a new column 'cell_density' to the DataFrame
    data['cell_density'] = np.nan

    for _, row in data.iterrows():
        # Predict cell density using the model
        cell_density = model.predict(pd.DataFrame([row], columns=feature_names))

        # Update the 'cell_density' column
        data.at[_, 'cell_density'] = cell_density
    
    # Save the DataFrame to an Excel file
    data.to_excel(output_excel_path, index=False)


