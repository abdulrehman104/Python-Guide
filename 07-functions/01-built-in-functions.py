# ====================================== Python Built-in Functions ======================================

# ========= print Function =========
# Description: Outputs text or variables to the console.
print("Hello, World!")


# ========= input Function =========
# Description: Reads a line of text from the user.
name = input("Enter your name: ")
print("Hello,", name)


# ========= len Function =========
# Description: Returns the number of items in a sequence.
fruits = ["apple", "banana", "cherry"]
print("Length of fruits list:", len(fruits))


# ========= type Function =========
# Description: Returns the data type of an object.
print("Type of 3.14 is", type(3.14))


# ========= int(), float(), str() Functions =========
# Description: Convert between integer, floating point, and string types.
print("int('10') ->", int("10"))
print("float('3.14') ->", float("3.14"))
print("str(100) ->", str(100))


# ========= sum Function =========
# Description: Sums all items of an iterable.
numbers = [10, 20, 30]
print("Sum of numbers:", sum(numbers))


# ========= max() / min() Functions =========
# Description: Returns the largest or smallest item in an iterable.
values = [5, 1, 9, 2]
print("Max value:", max(values))
print("Min value:", min(values))


# ========= sorted Function =========
# Description: Returns a new sorted list from an iterable.
nums = [3, 1, 4, 2]
print("Sorted list:", sorted(nums))


# ========= range Function =========
# Description: Generates a sequence of numbers.
print("Numbers from 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()


# ========= enumerate Function =========
# Description: Adds a counter to an iterable and returns pairs.
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(f"{idx}: {color}")


# ========= zip Function =========
# Description: Aggregates elements from multiple iterables.
names = ["Ali", "Sara"]
scores = [85, 92]
for n, s in zip(names, scores):
    print(n, "scored", s)


# ========= abs Function =========
# Description: Returns the absolute value of a number.
print("Absolute of -7 is", abs(-7))


# ========= round Function =========
# Description: Rounds a floating-point number to given precision.
print("Rounded 3.14159 to 2 decimals:", round(3.14159, 2))


# ========= pow Function =========
# Description: Returns base raised to the exponent (base**exp).
print("2 to the power 5 is", pow(2, 5))


# ========= all() / any() Functions =========
# Description: all() returns True if all items true; any() if any item true.
flags = [True, True, False]
print("all(flags):", all(flags))
print("any(flags):", any(flags))


# ========= bool Function =========
# Description: Converts a value to True or False.
print("bool(0):", bool(0))
print("bool('non-empty'):", bool("non-empty"))


# ========= help Function =========
# Description: Displays the documentation for an object.
help(len)  # Uncomment to view docs for len()
