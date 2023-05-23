from pybit.unified_trading import HTTP
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


class ByBitInstrument:

    def __init__(self):
        self.response = self.get_instrument()
        self.object = self.create_instrument_object()

    def get_instrument(self):
        session = HTTP(testnet=False, api_key=API_KEY, api_secret=API_SECRET,)
        response = session.get_instruments_info(
            category="linear",
            symbol="BTCUSDT",
            api_key="EKim1rHsFKKuAKybhe",
            secret_key="XhEbHQpwNpUpoDIwFdG3YAzRdrzvp5oyBhob",
        )
        return response

    def create_instrument_object(self):
        obj = {
            "Return Message": self.response["retMsg"],
            "Category": self.response["result"]["category"],
            "Symbol": self.response["result"]["list"][0]["symbol"],
            "Status": self.response["result"]["list"][0]["status"],
            "Base Coin": self.response["result"]["list"][0]["baseCoin"],
            "Quote Coin": self.response["result"]["list"][0]["quoteCoin"],
            "Launch Time": dt.fromtimestamp(int(self.response["result"]["list"][0]["launchTime"]) / 1000.0).isoformat(' '),
            "Min Price": self.response["result"]["list"][0]["priceFilter"]["minPrice"],
            "Max Price": self.response["result"]["list"][0]["priceFilter"]["maxPrice"],
            "Time": dt.fromtimestamp(int(self.response["time"]) / 1000.0).isoformat(' '),
        }
        return obj

    def write_instrument_to_file(self):
        with open("instrument.txt", 'w') as f:
            for key, value in self.object.items():
                f.write(f"{key} : {value}\n")

    def print_instrument_from_file(self):
        with open('instrument.txt', 'r') as f:
            for line in f:
                print(line.strip())
        return None

