import json

def load_call_prices():
    try:
        with open("phone_prices.json", "r") as file:
            prices = json.load(file)
            return prices
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading call prices:", e)
        return {}
