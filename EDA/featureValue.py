import matplotlib.pyplot as plt

def plot_unique_values(df, target_variable):
    unique_counts = df.drop(target_variable, axis=1).nunique()
    num_features = len(df.columns) - 1
    
    colors = ['#F9CF41' if df[column].dtype == 'object' else '#4E79A7' for column in df.drop(target_variable, axis=1).columns]
    
    fig, ax = plt.subplots(figsize=(10.6875, 4.245))
    bars = ax.barh(df.drop(target_variable, axis=1).columns, unique_counts, edgecolor='black', color=colors)
    ax.set_xlabel('Count of Unique Values')
    ax.set_ylabel('Features')
    
    ax.grid(axis='x', linestyle='dashed', color='gray', alpha=0.5)
    ax.set_axisbelow(True)
    
    # Create a legend
    legend_labels = ['Categorical', 'Numerical']
    legend_colors = ['#F9CF41', '#4E79A7']
    legend_elements = [plt.Rectangle((0, 0), 1, 1, color=color, edgecolor='black') for color in legend_colors]
    ax.legend(legend_elements, legend_labels, loc='lower right')
    
    plt.subplots_adjust(left=0.213, right=0.967)
    plt.savefig('D:\\DataProject\\venv\\inrhMicroalgae\\result\\uniqueValuePlot.png')
    plt.show()
