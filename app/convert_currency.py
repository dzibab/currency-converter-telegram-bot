import requests
from datetime import datetime, timezone

from api import EXCHANGE_API_KEY


_rates_cache = {}


def fetch_rates(from_currency: str) -> dict:
    today = datetime.now(tz=timezone.utc).date()
    cache_entry = _rates_cache.get(from_currency.upper())

    if cache_entry and cache_entry["date"] == today:
        return cache_entry["rates"]

    url = "https://api.exchangerate.host/live"
    params = {
        "access_key": EXCHANGE_API_KEY,
        "source": from_currency.upper()
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if not data["success"]:
        raise ValueError("API request failed")

    _rates_cache[from_currency.upper()] = {
        "date": today,
        "rates": data["quotes"]
    }

    return data["quotes"]


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rates = fetch_rates(from_currency)
    key = f"{from_currency.upper()}{to_currency.upper()}"
    rate = rates.get(key)
    if rate is None:
        raise ValueError(f"Conversion rate not found for {key}")
    return round(amount * rate, 4)


if __name__ == "__main__":
    while True:
        amount_input = input("Enter the amount to convert (or type 'exit' to quit): ")
        if amount_input.lower() == "exit":
            print("Exiting the currency converter. Goodbye!")
            break

        try:
            amount = float(amount_input)
            from_currency = input("Enter the currency to convert from (e.g., USD): ")
            to_currency = input("Enter the currency to convert to (e.g., EUR): ")

            converted_amount = convert_currency(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching conversion rate: {e}")
        except KeyError:
            print("Invalid currency code.")
