import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON:", json_str)

loaded = json.loads(json_str)
print("Loaded:", loaded)
