import pandas as pd
from sklearn.preprocessing import StandardScaler

def scaling_and_save(df_scaled, numerical_features):
    scaler = StandardScaler()
    df_scaled[numerical_features] = scaler.fit_transform(df_scaled[numerical_features])
    df_scaled = df_scaled.reset_index(drop=True)  # Reset to a continuous index
    # Save the scaled DataFrame to an Excel file
    df_scaled.to_excel('D:\\DataProject\\venv\\inrhMicroalgae\\Import\\scaled_data.xlsx', index=False, engine='xlsxwriter')

    return df_scaled