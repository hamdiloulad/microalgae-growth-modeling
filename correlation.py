import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df):
    # Calculate correlation matrix
    corr_matrix = df.corr()

    # Plot correlation heatmap
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.176)
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig('D:\\DataProject\\venv\\inrhMicroalgae\\result\\heatMap.png')
    plt.show()
