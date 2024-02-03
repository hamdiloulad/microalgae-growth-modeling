import numpy as np
from sklearn.impute import KNNImputer
from sklearn.metrics import mean_squared_error

def TuningKnnImputing(df, all_features, n_neighbors, metric, weights):
    imputer_all = KNNImputer(n_neighbors=n_neighbors, metric=metric, weights=weights)

    data = df.dropna()
    test_set = data.copy()
    test_set['CellDensity'].mask(np.random.random(test_set['CellDensity'].shape) < 0.1, inplace=True)
    imputed_values = imputer_all.fit_transform(test_set[all_features])
    
    # Extract imputed values for the target feature using the column name
    imputed_values_target= imputed_values[:, all_features.index('CellDensity')]
    
    true_values = data['CellDensity'].values
    mse = mean_squared_error(true_values, imputed_values_target)
    rmse = np.sqrt(mse)
    return rmse

