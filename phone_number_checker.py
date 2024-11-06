from price_loader import load_call_prices
from phone_utils import parse_phone_number, get_country_and_region, get_operator, get_time_zones, get_number_type, get_call_price, is_possible_number
from output_formatter import format_output
import phonenumbers

# Load call prices
call_prices = load_call_prices()

def get_phone_number():
    phone_number = input("Enter phone number (with country code, e.g., +1234567890): ").strip()
    if not phone_number:
        print("Phone number cannot be empty.")
        return None
    return phone_number

def display_phone_number_info(phone_number, language="en", json_output=False):
    parsed_number = parse_phone_number(phone_number)
    if parsed_number:
        info = {
            "International Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "Country": get_country_and_region(parsed_number, language)[0],
            "Region": get_country_and_region(parsed_number, language)[1],
            "Operator": get_operator(parsed_number, language),
            "Time Zones": ", ".join(get_time_zones(parsed_number)),
            "Number Type": get_number_type(parsed_number),
            "Is Possible Number": "Yes" if is_possible_number(parsed_number) else "No",
            "Call Price (€/min)": get_call_price(parsed_number, call_prices)
        }
        format_output(info, json_output=json_output)
    else:
        print("Could not retrieve information due to an invalid phone number.")

# Run the main function to get and display information about the phone number
phone_number = get_phone_number()
if phone_number:
    display_phone_number_info(phone_number, language="en", json_output=True)
