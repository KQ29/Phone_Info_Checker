import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, is_possible_number
import json

# Function to get the phone number input from the user
def get_phone_number():
    phone_number = input("Enter phone number (with country code, e.g., +1234567890): ").strip()
    # Check if the input is empty
    if not phone_number:
        print("Phone number cannot be empty.")
        return None
    return phone_number

# Function to parse and validate the phone number
def parse_phone_number(phone_number):
    try:
        # Parse the phone number using phonenumbers library
        parsed_number = phonenumbers.parse(phone_number)
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number format.")
            return None
        return parsed_number
    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
        return None

# Function to get country and region information
def get_country_and_region(parsed_number, language="en"):
    country = geocoder.description_for_number(parsed_number, language)
    region = geocoder.description_for_number(parsed_number, language)
    return country, region

# Function to get the carrier (operator) information
def get_operator(parsed_number, language="en"):
    return carrier.name_for_number(parsed_number, language)

# Function to get the time zones associated with the number
def get_time_zones(parsed_number):
    return timezone.time_zones_for_number(parsed_number)

# Function to get the type of phone number (e.g., mobile, landline)
def get_number_type(parsed_number):
    # Mapping of number types to readable names
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

# Function to format and print output in either JSON or plain text
def format_output(info_dict, json_output=False):
    if json_output:
        print(json.dumps(info_dict, indent=4))
    else:
        for key, value in info_dict.items():
            print(f"{key}: {value}")

# Main function to display information about the phone number
def display_phone_number_info(phone_number, language="en", json_output=False):
    # Parse the phone number
    parsed_number = parse_phone_number(phone_number)
    if parsed_number:
        # Gather information about the phone number
        info = {}
        info["International Format"] = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        info["Country"], info["Region"] = get_country_and_region(parsed_number, language)
        info["Operator"] = get_operator(parsed_number, language)
        info["Time Zones"] = ", ".join(get_time_zones(parsed_number))
        info["Number Type"] = get_number_type(parsed_number)
        info["Is Possible Number"] = "Yes" if is_possible_number(parsed_number) else "No"
        
        # Output the gathered information
        format_output(info, json_output=json_output)
    else:
        print("Could not retrieve information due to an invalid phone number.")

# Run the main function to get and display information about the phone number
phone_number = get_phone_number()
if phone_number:
    display_phone_number_info(phone_number, language="en", json_output=True)
