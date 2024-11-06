import phonenumbers 
from phonenumbers import geocoder, carrier, timezone, number_type, is_possible_number
import json 

def get_phone_number():
    phone_number = input("Enter phone number (with country code., +1234567890): ").strip()

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
        print("Error paring phone number: {e}")
        return None
    
def get_country_and_region(parsed_number, language="en"):
    country = geocoder.description_for_number(parsed_number, language)
    region = geocoder.description_for_number(parsed_number, language)
    return country, region

def get_operator(parsed_number, language="en"):
    return carrier.name_for_number(parsed_number, language)

def get_time_zones(parsed_number):
    return timezone.time_zones_for_number(parsed_number)
