import numpy as np
import pandas as pd

def find_optimal_cell_density(model, feature_names, data):
    max_cell_density = float('-inf')
    optimal_feature_values = None

    for _, row in data.iterrows():
        # Predict cell density using the model
        cell_density = model.predict(pd.DataFrame([row], columns=feature_names))

        # Update max_cell_density and optimal_feature_values if needed
        if cell_density > max_cell_density:
            max_cell_density = cell_density
            optimal_feature_values = row
    
    return max_cell_density, dict(zip(feature_names, optimal_feature_values))
