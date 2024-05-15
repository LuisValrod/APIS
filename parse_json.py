import json

# json.load() --> Takes a file and converts to a dictionary

# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])

path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.load(jsonfile)
value = json_data["name"]

print(value)
# json.loads() --> takes a string and convert it into a dictionary

path_to_json = "example.json"
with open(path_to_json) as jsonfile:
    json_data = json.loads(jsonfile.read())
    print(jsonfile.read())
    print(json_data)
# value = json_data["name"]
#
# print(value)
