import numpy as np
import matplotlib.pyplot as plt

def plot_variable_importances(model, feature_names, colors=['#F28E2B', '#4E79A7', '#EDC948', '#75B7B2', '#E15658','#59A14F','#DAE3F3','#B40426']):
    # Get feature importances from the model
    importances = model.feature_importances_

    # Sort feature importances in descending order
    indices = np.argsort(importances)[::-1]

    # Rearrange feature names and importances based on the sorted order
    sorted_feature_names = feature_names[indices]
    sorted_importances = importances[indices]

    # Create a pie chart
    plt.figure(figsize=(8, 8))  # Adjust the figure size if needed
    wedges, _ = plt.pie(sorted_importances, labels=None, autopct=None, colors=colors)

    # Add legend with feature names, importance values, and colors
    plt.legend(wedges, sorted_feature_names, title='Feature Importance', loc='center left', bbox_to_anchor=(1, 0.5))

    # Add title
    plt.title('Feature Importance')

    # Show the plot
    plt.show()

