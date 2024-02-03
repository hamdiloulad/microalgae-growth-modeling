import pandas as pd

def encode_and_save(df, one_hot_features):

    # One-hot encoding for specified features
    df_encoded = pd.get_dummies(df, columns=one_hot_features)
    # Save to Excel file
    df_encoded.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\encoded.xlsx', index=False)

    return df_encoded

