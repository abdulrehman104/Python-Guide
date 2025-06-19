import json

# # Reading JSON data from a file
# # This will read the JSON data from 'data.json' and parse it into a Python dictionary
# with open("data.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)
# print(loaded["name"])  # Alice
# print(loaded["age"])  # 30
# print(loaded["hobbies"])  # ['reading', 'hiking']


# # Writing JSON data to a file
# # This will create a new file named 'data.json' and write the JSON data into it
# data = {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]}
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2)       # pretty-print with indent of 2 spaces


# # Append JSON data to a file
# # This will read existing data, append new data, and write it back to the file
# data = {"name": "Bob", "age": 25, "hobbies": ["gaming", "cooking"]}

# with open("data.json", "a", encoding="utf-8")as f:
#     json.dump(data, f, indent=2)



new_entry = {"name": "Rehman", "age": 25, "hobbies": ["gaming", "cooking"]}

# 1. Read existing data (or start with an empty list if file is missing or invalid)
try:
    with open("data.json", "r+", encoding="utf-8") as f:
        existing_data = json.load(f)
        if not isinstance(existing_data, list):
            # If the file contains a single object, wrap it in a list
            existing_data = [existing_data]
except (FileNotFoundError, json.JSONDecodeError):
    existing_data = []

# 2. Append your new entry
existing_data.append(new_entry)

# 3. Write the updated list back, truncating any old content
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, indent=2)