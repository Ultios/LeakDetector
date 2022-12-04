def preparingData():
    df_raw = pd.read_excel("data.xlsx")
    df = df_raw[["delta pressure", "Leak rate (STB/d)", "leak_location"]]
    return df

def preprocessingData(df):
    X = df.iloc[:, :2]
    y = df["leak_location"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
    return X_train, X_test, y_train, y_test