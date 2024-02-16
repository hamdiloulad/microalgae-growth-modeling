import pandas as pd
import joblib

def rescale(df_new, numerical_features, scaler_filename='custom_scaler_model.pkl'):
    scaler = joblib.load(scaler_filename)
    df_new[numerical_features] = scaler.inverse_transform(df_new[numerical_features])
    df_new.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\cleaned_data.xlsx', index=False, engine='xlsxwriter')

    return df_new


