# ====================================== Dictionary ======================================

# A dictionary in Python is a collection of key-value pairs. Each key is unique.

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing Elements
print(person["name"])                     # John
print(person.get("name"))                 # John
print(person.get("gender", "Not Found"))  # Not Found

# Adding / Updating Elements
person["country"] = "USA"    # add new
person["city"]    = "London" # update existing

# Removing Elements
del person["age"]
print(person)  # {'name': 'John', 'city': 'London', 'country': 'USA'}

# Checking Existence
if "name" in person:
    print("Key exists")      # Key exists

# Iterating Over a Dictionary
for key in person:
    print("Key:", key)
for value in person.values():
    print("Value:", value)
for key, value in person.items():
    print(f"{key} → {value}")


# ====================================== List ======================================

# Lists are ordered, mutable collections allowing duplicates.

numbers = [10, 20, 30, 40]

# Accessing Elements
print(numbers[0])    # 10
print(numbers[-1])   # 40

# Slicing
print(numbers[1:3])  # [20, 30]

# Appending / Inserting
numbers.append(50)
numbers.insert(2, 15)
print(numbers)       # [10, 20, 15, 30, 40, 50]

# Removing
numbers.pop()        # removes 50
numbers.remove(15)   # removes first 15
print(numbers)       # [10, 20, 30, 40]

# Mutability
numbers[0] = 99
print(numbers)       # [99, 20, 30, 40]

# Iterating
for idx, num in enumerate(numbers):
    print(f"Index {idx} → {num}")


# ====================================== Strings ======================================

# Strings are immutable sequences of characters.

first_name = "John"
last_name  = "Doe"
full_name  = first_name + " " + last_name  # concatenation
print(full_name)     # John Doe

# Repetition
print("ha" * 3)      # hahaha

# Indexing / Slicing
greeting = "Hello"
print(greeting[0])   # H
print(greeting[1:5]) # ello

# Common Methods
print(greeting.upper())        # HELLO
print(greeting.lower())        # hello
print(greeting.replace("l", "L"))  # HeLLo
print(greeting.split("l"))     # ['He', '', 'o']

# f-strings
age = 25
print(f"My age is {age}")      # My age is 25


# ====================================== Tuple ======================================

# Tuples are ordered, immutable collections.

person_tuple = ("Bob", 30, "Engineer")

# Accessing / Slicing
print(person_tuple[0])   # Bob
print(person_tuple[1:])  # (30, 'Engineer')

# Immutability (will error if uncommented)
# person_tuple[1] = 35

# Unpacking
name, age, job = person_tuple
print(name, age, job)    # Bob 30 Engineer
