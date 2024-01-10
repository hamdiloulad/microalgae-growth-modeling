import pandas as pd
from histogramPlot import create_histogram
from boxPlot import plot_boxplot
from dataInfo import display_dataframe_info
from featureValue import plot_unique_values

excel_file_path = 'D:\\DataProject\\venv\\inrhMicroalgae\\Import\\data.xlsx'
df = pd.read_excel(excel_file_path)
plot_unique_values(df,"CellDensity")
display_dataframe_info(df)
create_histogram(df, 'CellDensity')
plot_boxplot(df, 'CellDensity')


