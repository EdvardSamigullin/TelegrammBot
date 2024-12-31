import json
import requests
from config import keys
class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/53e8155499fb7acfa02a0ca8/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']
        total = format(total_base*amount, '.5f')
        return total