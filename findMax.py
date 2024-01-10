import numpy as np
import pandas as pd
from itertools import product

def find_optimal_cell_density(model, feature_names, *feature_values):
    max_cell_density = float('-inf')
    optimal_feature_values = None

    # Generate all possible combinations of feature values
    combinations = list(product(*feature_values))

    for values in combinations:
        modified_feature_values = np.array(values).reshape(1, len(feature_names))
        df = pd.DataFrame(modified_feature_values, columns=feature_names)
      # Create a DataFrame with feature names
        cell_density = model.predict(df)
        
        if cell_density > max_cell_density:
            max_cell_density = cell_density
            optimal_feature_values = values
    
    return max_cell_density, dict(zip(feature_names, optimal_feature_values))