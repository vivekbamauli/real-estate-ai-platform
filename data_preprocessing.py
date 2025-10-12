import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df["price_per_sqft"] = df["price"] / df["area_sqft"]
    return df

if __name__ == "__main__":
    df = load_and_clean_data("data/properties.csv")
    print(df.head())
