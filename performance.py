import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

def evaluate_regression_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # Print the performance indicators
    print("Mean Squared Error (MSE):", mse)
    print("Root Mean Squared Error (RMSE):", rmse)
    print("Mean Absolute Error (MAE):", mae)
    print("R-squared (R2):", r2)
    
    # Return the performance indicators as a dictionary
    performance = {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    }
    indicators = ["MSE", "RMSE", "MAE", "R2"]
    values = [mse, rmse, mae, r2]
    
    plt.bar(indicators, values)
    plt.xlabel("Indicators")
    plt.ylabel("Value")
    plt.title("Performance Indicators")
    plt.show()
    return performance
