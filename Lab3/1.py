import json
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
python_data = json.loads(json_data)
print("Deserialized JSON Data:", python_data)
