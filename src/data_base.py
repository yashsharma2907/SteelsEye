import pandas as pd
from pandas import DataFrame


class DataBase:
    def __init__(self, src: str):
        self.df = pd.read_csv(src)

    def head(self) -> DataFrame:
        return self.df.head()

    def to_json(self):
        return self.df.to_json(orient="records")


if __name__ == "__main__":
    db = DataBase("../data/data.csv")
    print(db.head())
