import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Handle missing values (fill with mean or drop)
    df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
    df['precipitation'] = df['precipitation'].fillna(0)
    df['humidity'] = df['humidity'].fillna(df['humidity'].mean())

    return df
