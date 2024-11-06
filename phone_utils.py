import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, is_possible_number

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

def get_call_price(parsed_number, call_prices):
    dialing_code = f"+{parsed_number.country_code}"
    price_info = call_prices.get(dialing_code)
    if price_info:
        return price_info.get("rate_eur_per_min", "Not Available")
    return "Not Available"
