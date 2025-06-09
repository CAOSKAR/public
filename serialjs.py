import json
# Sample data
data = {'name': 'Alice', 'age': 30, 'is_student': False}

# Serialization
with open('data.json', 'w') as file:
    json.dump(data, file)

# Deserialization
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)

# Output:
# =======
# {'name': 'Alice', 'age': 30, 'is_student': False}