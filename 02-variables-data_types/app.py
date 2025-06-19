# ======================================
# Variable Assignment & Data Types Demo
# ======================================

# Basic Assignments
fruit      = "apple"     # string
a          = 10          # integer
price      = 99.99       # float
is_active  = True        # boolean


# Multiple Assignment (same value)
x = y = z = 0
print(x, y, z)           # 0 0 0


# Multiple Assignment (different values)
first, second, third = 1, 2, 3
print(first, second, third)  # 1 2 3


# Swapping Variables (no temp needed)
first, second = second, first
print(first, second)      # 2 1


# Case Sensitivity
FirstName = "Ali"
firstname = "Ahmed"
print(FirstName, firstname)   # Ali Ahmed


# Naming Conventions (valid examples)
user_name   = "john_doe"      # snake_case
userName    = "janeDoe"       # camelCase
UserName    = "Admin"         # PascalCase (often for classes)


# Constants (by convention, all caps)
PI      = 3.14159
MAX_ATTEMPTS = 5


# Type Conversion (casting)
num_str   = "42"
num_int   = int(num_str)       # from str to int
num_float = float(num_int)     # from int to float
print(num_int, num_float)      # 42 42.0


# Deleting a Variable
temp = "to be deleted"
del temp
# print(temp)  # NameError: temp is not defined


# Dynamic Typing (reassigning different types)
var = 100           # var is int
print(type(var))    # <class 'int'>
var = "hello"       # now var is str
print(type(var))    # <class 'str'>


# Invalid Variable Names (uncomment to see errors)
# 1user = "Ali"      # SyntaxError: cannot start with a number
# print = 10         # Not recommended: shadowing built-in function
