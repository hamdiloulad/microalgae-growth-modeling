import pandas as pd
import matplotlib.pyplot as plt

def plot_boxplot(df, feature_name):
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

    # Create the box plot
    df.boxplot(column=feature_name)

    # Customize the plot
    plt.title('Box Plot of {}'.format(feature_name))
    plt.ylabel('{}'.format(feature_name))

    plt.savefig('D:\\DataProject\\venv\\inrhMicroalgae\\result\\boxplot.png')
    # Display the box plot
    plt.show()
