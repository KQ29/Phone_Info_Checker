import json

def format_output(info_dict, json_output=False):
    if json_output:
        print(json.dumps(info_dict, indent=4))
    else:
        for key, value in info_dict.items():
            print(f"{key}: {value}")
