# __author__ == "Priya"

import os
import json
import forex_python
from collections import defaultdict
from forex_python.converter import CurrencyRates


class CurrencyConverter():
    def __init__(self):
        self.FOLDER_PATH = os.path.dirname(forex_python.__file__)
        self.FILE_PATH = os.path.join(self.FOLDER_PATH, 'raw_data//currencies.json')
        self.c = CurrencyRates()

    def get_currencies_data(self):
        with open(self.FILE_PATH) as f:
            json_data = json.loads(f.read())
        currencies_data = defaultdict(dict)
        currencies_data = {k['cc']:{k1:v1 for k1, v1 in k.items() if k1 != 'cc'} for k in json_data}
        return currencies_data

    def convert_currency(self, from_code, to_code, value):
        result = self.c.convert(from_code, to_code, float(value))
        return result

    def get_symbol(self,code):
        data = self.get_currencies_data()
        symbol = data[code].get('symbol')
        return symbol

    def get_rates(self,code):
        try:
            rates = self.c.get_rates(code)
            return rates
        except:
            return None