import pickle

# Sample data
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Serialization
with open('complex_data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialization
with open('complex_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

# Output:
# =======
# [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]