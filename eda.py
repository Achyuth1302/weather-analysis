def perform_eda(df):
    print("\n--- Dataset Info ---")
    print(df.info())

    print("\n--- Basic Statistics ---")
    print(df.describe())

    print("\n--- Null Values ---")
    print(df.isnull().sum())
