from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

from data_base import DataBase

db = DataBase("../data/data.csv")
df = db.df
app = FastAPI()


@app.get("/")
def home():
    return "hello from my api"


@app.get("/trade")
def get_trade(trade_id: Union[str, None]):
    value = df.loc[df["trade_id"] == trade_id]
    return value.to_dict(orient="records")


@app.get("/trades")
def get_trade(search: Union[str, None]):
    value = df[(df == search).any(axis=1)]
    return value.to_dict(orient="records")


@app.get("/trades/filter")
def get_trade(assetClass: Union[str, None] = None,
              end: Union[str, None] = None,
              minPrice: Union[str, None] = None,
              maxPrice: Union[str, None] = None,
              start: Union[str, None] = None,
              tradeType: Union[str, None] = None):
    value = df
    if assetClass:
        value = value.loc[value["asset_class"] == assetClass]
    if end:
        value = value[(value['trade_date_time'] < end)]
    if start:
        value = value[(value['trade_date_time'] > start)]
    if maxPrice:
        value = value[(value['price'] < maxPrice)]
    if minPrice:
        value = value[(value['price'] > minPrice)]
    if tradeType:
        value = value.loc[value["buySellIndicator"] == tradeType]

    return value.to_dict(orient="records")
