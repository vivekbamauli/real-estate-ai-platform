import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from index_calculator import calculate_liveability, calculate_viability

def train_model(df):
    df["Liveability_Index"] = df.apply(calculate_liveability, axis=1)
    df["Viability_Score"] = df.apply(calculate_viability, axis=1)

    X = df[["Liveability_Index", "Viability_Score", "rent_yield", "crime_rate", "pollution_index"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    preds = model.predict(X_test)

    print("Model R² Score:", r2_score(y_test, preds))
    return model

if __name__ == "__main__":
    df = pd.read_csv("data/properties.csv")
    model = train_model(df)
