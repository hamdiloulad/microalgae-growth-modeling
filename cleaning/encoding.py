import pandas as pd

def encode_and_save(df, one_hot_features):

    df_encoded = pd.get_dummies(df, columns=one_hot_features)
    df_encoded.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\encoded.xlsx', index=False)

    return df_encoded

