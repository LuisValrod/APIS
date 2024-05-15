import json # Don't call a file json to avoid errors
import requests

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))

# json.dumps() --> turn python dict to a str
car_data_json_string = json.dumps(car_data)
print (car_data_json_string)
print(type(car_data_json_string))

# json.dump() --> Convert dict to a str and store in a file

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile, indent=4)
