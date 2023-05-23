from pybit.unified_trading import HTTP
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


class ByBitKline:

    def __init__(self):
        self.response = self.get_kline()
        self.object = self.create_kline_object()

    def get_kline(self):
        session = HTTP(testnet=False, api_key=API_KEY, api_secret=API_SECRET,)
        response = session.get_kline(
            category="linear",
            symbol="BTCUSD",
            interval=60,
            start=1670601600000,
            end=1670608800000,
        )
        return response

    def create_kline_object(self):
        lists = {
            "List1": self.response["result"]["list"][0],
            "List2": self.response["result"]["list"][1],
            "List3": self.response["result"]["list"][2],
        }
        obj = {
            "Return Message": self.response["retMsg"],
            "Category": self.response["result"]["category"],
            "Symbol": self.response["result"]["symbol"],
            "Time": dt.fromtimestamp(int(self.response["time"]) / 1000.0).isoformat(' '),
        }
        for key, value in lists.items():
            dct = {
                f"{key} Start time of the candle": dt.fromtimestamp(int(value[0]) / 1000.0).isoformat(' '),
                f"{key} Open price": value[1],
                f"{key} Highest price": value[2],
                f"{key} Lowest price": value[3],
                f"{key} Close price": value[4],
                f"{key} Trade Volume": value[5],
                f"{key} Turnover": value[6],
            }
            obj.update(dct)
        return obj

    def write_kline_to_file(self):
        with open("kline.txt", 'w') as f:
            for key, value in self.object.items():
                f.write(f"{key} : {value}\n")

    def print_kline_from_file(self):
        with open('kline.txt', 'r') as f:
            for line in f:
                print(line.strip())
        return None

