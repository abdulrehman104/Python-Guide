# ====================================== Loops Syntax ======================================

# ---- For Loop ----
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print()  # blank line

# ---- While Loop ----
count = 0
while count < 5:
    print(count)
    count += 1

print("\n")  # two blank lines



# ====================================== Control Statements in Loops ======================================

# ---- Continue Statement ----
for i in range(10):
    if i == 3:
        print("Skipping 3")
        continue
    print(i)

print("\n")  # two blank lines

# ---- Break Statement ----
for i in range(10):
    if i == 8:
        print("Breaking at 8")
        break
    print(i)

print("\n")  # two blank lines

# ---- Else Statement ----
for i in range(5):
    if i < 3:
        print(i)
    else:
        print("Loop ended naturally")

print("\n")  # two blank lines



# ====================================== Working with Lists and Indexing ======================================

# ---- Enumerate Function ----
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()  # blank line

# ---- Manual Indexing ----
fruits = ["apple", "banana", "cherry"]
index = 0
for fruit in fruits:
    print(f"Index {index}: {fruit}")
    index += 1

print("\n")  # two blank lines



# ====================================== Iterating Over Dictionaries ======================================

# ---- Iterating Over Keys ----
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)

print()  # blank line

# ---- Iterating Over Values ----
for value in person.values():
    print(value)

print()  # blank line

# ---- Iterating Over Key-Value Pairs ----
for key, value in person.items():
    print(f"{key}: {value}")
