import pandas as pd

def split_photoperiod(df):
    # Split the values in the 'photoperiod' column
    df[['lightTime', 'darkTime']] = df['Photoperiod'].str.split('/', expand=True)
    # Convert the columns to numeric values
    df['lightTime'] = pd.to_numeric(df['lightTime'])
    df['darkTime'] = pd.to_numeric(df['darkTime'])
    # Return the modified DataFrame
    df.drop("Photoperiod", axis=1, inplace=True)
    return df
