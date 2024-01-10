import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from performance import evaluate_regression_model
from modelSelection import selection
from featureImportance import plot_variable_importances
def regression_model(df, features, target):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

    # Split the remaining data into validation and testing sets
    X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
    
    bestModel = selection(X_val, y_val, X_train, y_train)
    model = RandomForestRegressor(max_depth=7)
    model.fit(X_train, y_train)
    feature_names = np.array(features)
    plot_variable_importances(model, feature_names)
    y_pred = model.predict(X_test)
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)

    # Calculate RMSE for train and validation data
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    val_rmse = np.sqrt(mean_squared_error(y_val, y_val_pred))

    print("Train RMSE:", train_rmse)
    print("Validation RMSE:", val_rmse)
    # Evaluate the performance
    performance = evaluate_regression_model(y_test, y_pred)

    # Return the trained model
    return model
