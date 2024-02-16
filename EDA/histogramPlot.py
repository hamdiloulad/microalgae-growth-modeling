import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_histogram(df, feature_name):
    fig, ax = plt.subplots(figsize=(7.14, 2.655))  

    # Create the histogram
    bin_width = 0.5
    bins = np.arange(df[feature_name].min(), df[feature_name].max() + bin_width, bin_width)
    plt.hist(df[feature_name], bins=bins, edgecolor='black', color='#4E79A7')

    # Customize the plot
    plt.title('Histogram of {}'.format(feature_name))
    plt.xlabel(feature_name)
    plt.ylabel('Frequency')

    ax.grid(axis='y', linestyle='dashed', color='gray', alpha=0.5)
    ax.set_axisbelow(True)

    plt.savefig('D:\\DataProject\\venv\\inrhMicroalgae\\result\\histogram.png')
    # Display the histogram
    plt.show()
    
