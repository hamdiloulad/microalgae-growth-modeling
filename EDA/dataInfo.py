
import pandas as pd
def display_dataframe_info(df):

    col_names = df.columns.tolist()

    col_types = df.dtypes.tolist()

    unique_counts = df.nunique().tolist()


    min_values = df.min().tolist()

    max_values = df.max().tolist()

    table_data = {
        'Feature': col_names,
        'Type': col_types,
        'Unique Count': unique_counts,
        'Min': min_values,
        'Max': max_values,
    }

    info_df = pd.DataFrame(table_data)
    print(info_df)
