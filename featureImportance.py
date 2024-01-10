import numpy as np
import matplotlib.pyplot as plt

def plot_variable_importances(model, feature_names):
    # Get feature importances from the model
    importances = model.feature_importances_

    # Sort feature importances in descending order
    indices = np.argsort(importances)[::-1]

    # Rearrange feature names and importances based on the sorted order
    sorted_feature_names = feature_names[indices]
    sorted_importances = importances[indices]

    # Create a horizontal bar chart
    plt.barh(sorted_feature_names, sorted_importances, color='blue')

    # Add labels and title
    plt.xlabel('Importance')
    plt.ylabel('Features')
    plt.title('Feature Importance')

    # Show the plot
    plt.show()
