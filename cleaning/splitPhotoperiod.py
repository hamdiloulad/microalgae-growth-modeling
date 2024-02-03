import pandas as pd

def split_photoperiod(df):
    df = df.copy()
    df[['lightTime', 'darkTime']] = df['Photoperiod'].str.split('/', expand=True)
    df.loc[:, 'lightTime'] = pd.to_numeric(df['lightTime'])
    df.loc[:, 'darkTime'] = pd.to_numeric(df['darkTime'])
    df.drop("Photoperiod", axis=1, inplace=True)
    df.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\split.xlsx', index=False)
    return df
