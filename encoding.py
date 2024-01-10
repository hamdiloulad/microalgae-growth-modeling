import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_and_save(df, one_hot_features):


    # One-hot encoding for specified features
    df_encoded = pd.get_dummies(df, columns=one_hot_features)

    # Label encoding for specified feature
    label_encoder = LabelEncoder()


    # Save to Excel file
    df_encoded.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\encoded.xlsx', index=False)

    return df_encoded

