import phonenumbers 
from phonenumbers import geocoder, carrier, timezone, number_type, is_possible_number
import json 

def get_phone_number():
    phone_number = input("Enter phone number (with country code., +1234567890): ").strip()

    if not phone_number:
        print("Phone number cannot be empty.")
        return None
    return phone_number