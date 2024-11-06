import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, is_possible_number
import json

# Function to load call prices from phone_prices.json
def load_call_prices():
    try:
        with open("phone_prices.json", "r") as file:
            prices = json.load(file)
            return prices
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading call prices:", e)
        return {}

# Load call prices into a dictionary
call_prices = load_call_prices()

def get_phone_number():
    phone_number = input("Enter phone number (with country code, e.g., +1234567890): ").strip()
    if not phone_number:
        print("Phone number cannot be empty.")
        return None
    return phone_number

def parse_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number format.")
            return None
        return parsed_number
    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
        return None

def get_country_and_region(parsed_number, language="en"):
    country = geocoder.description_for_number(parsed_number, language)
    region = geocoder.description_for_number(parsed_number, language)
    return country, region

def get_operator(parsed_number, language="en"):
    return carrier.name_for_number(parsed_number, language)

def get_time_zones(parsed_number):
    return timezone.time_zones_for_number(parsed_number)

def get_number_type(parsed_number):
    types = {
        phonenumbers.PhoneNumberType.MOBILE: "Mobile",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-Free",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
        phonenumbers.PhoneNumberType.VOIP: "VoIP",
        phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        phonenumbers.PhoneNumberType.PAGER: "Pager",
        phonenumbers.PhoneNumberType.UAN: "UAN",
        phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
        phonenumbers.PhoneNumberType.UNKNOWN: "Unknown",
    }
    return types.get(number_type(parsed_number), "Unknown")

def get_call_price(parsed_number):
    dialing_code = f"+{parsed_number.country_code}"
    price_info = call_prices.get(dialing_code)  # Retrieves the nested dictionary for the country
    if price_info:
        return price_info.get("rate_eur_per_min", "Not Available")  # Accesses the rate within the nested dictionary
    return "Not Available"

def format_output(info_dict, json_output=False):
    if json_output:
        print(json.dumps(info_dict, indent=4))
    else:
        for key, value in info_dict.items():
            print(f"{key}: {value}")

def display_phone_number_info(phone_number, language="en", json_output=False):
    parsed_number = parse_phone_number(phone_number)
    if parsed_number:
        info = {}
        info["International Format"] = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        info["Country"], info["Region"] = get_country_and_region(parsed_number, language)
        info["Operator"] = get_operator(parsed_number, language)
        info["Time Zones"] = ", ".join(get_time_zones(parsed_number))
        info["Number Type"] = get_number_type(parsed_number)
        info["Is Possible Number"] = "Yes" if is_possible_number(parsed_number) else "No"
        info["Call Price (€/min)"] = get_call_price(parsed_number)
        
        format_output(info, json_output=json_output)
    else:
        print("Could not retrieve information due to an invalid phone number.")

# Run the main function to get and display information about the phone number
phone_number = get_phone_number()
if phone_number:
    display_phone_number_info(phone_number, language="en", json_output=True)
