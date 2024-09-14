from prompt import get_values_from_input
from currency_converter import CurrencyConverter
import logging


def converter(input_json):
    try:
        amount, from_currency, to_currency = (
            input_json["amount"],
            input_json["source_currency"],
            input_json["destination_currency"],
        )
        c = CurrencyConverter()
        result = c.convert(amount, from_currency.upper(), to_currency.upper())
        return f"{to_currency} {result}"
    except ValueError:
        return "Unsupported Currency"
    except KeyError:
        logging.error("Malformed Query. e.g. query \n/convert 3000 inr to usd")


def convert_handler(input_text):
    input_json = get_values_from_input(input_text)
    if "error" in input_json:
        result = "Invalid/Malformed Query. e.g. query \n/convert 3000 inr to usd"
        status_code = 400
    else:
        result = converter(input_json)
    return result
