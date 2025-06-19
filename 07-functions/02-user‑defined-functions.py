# ================== Basic User-Defined Functions ==================

def greet(name):
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")
    return None


# Call the function
greet("Alice")


# ================== Function with Parameters & Return ==================

def add(a, b):
    """Function to add two numbers."""
    return a + b


# Call the function and store the result
result = add(5, 3)
print(f"The sum is: {result}")


# ================== Function with Default Parameters ==================
def greet(name="World"):
    """Function to greet a person with their name. Default is 'World'."""
    print(f"Hello, {name}!")


# Call the function without an argument
greet()


# ================== Variable‑Length Arguments (*args, **kwargs) ==================

# *args allows for variable-length positional arguments
def print_args(*args):
    """Function to print variable-length arguments."""
    for arg in args:
        print(arg)


# Call the function with multiple arguments
print_args("Python", "is", "fun")


# **kwargs allows for variable-length keyword arguments
def print_kwargs(**kwargs):
    """Function to print variable-length keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Call the function with keyword arguments
print_kwargs(name="Alice", age=30, city="New York")


# ================== Multiple Return Values ==================
def calculate(a, b):
    """Function to perform basic arithmetic operations."""
    return a + b, a - b, a * b, a / b


# Call the function and unpack the returned values
sum, diff, prod, quot = calculate(10, 5)
print(f"Sum: {sum}, Difference: {diff}, Product: {prod}, Quotient: {quot}")


# ================== Lambda (Anonymous) Functions ==================

# Example 01:
# Lambda function for squaring a number
def square(x): return x ** 2


# Call the lambda function
result = square(5)
print(f"The square of 5 is: {result}")


# Example 02:
# Lambda function for adding two numbers
def add(x, y): return x + y


# Call the lambda function
result = add(3, 4)
print(f"The sum of 3 and 4 is: {result}")


# ================== Recursion ==================

# Example 01:
# Recursive function to calculate factorial
def factorial(n):
    """Function to calculate the factorial of a number."""

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Call the recursive function
result = factorial(5)
print(f"The factorial of 5 is: {result}")


# Example 02:

# Recursive function to calculate the sum of a list
def sum_list(lst):
    """Function to calculate the sum of a list."""
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


# Call the recursive function
result = sum_list([1, 2, 3, 4, 5])
print(f"The sum of the list is: {result}")


# ================== Nested Functions & Closures ==================
# # Example 01:
# # Nested function to demonstrate closures
def outer_function(x):
    """Outer function that defines a nested function."""

    def inner_function(y):
        """Inner function that uses the outer function's variable."""
        return x + y

    return inner_function


# # Call the outer function and store the returned inner function
add_five = outer_function(5)
# # Call the inner function with an argument
result = add_five(10)
print(f"The result of adding 5 and 10 is: {result}")


# # Example 02:
# # Nested function to demonstrate closures
def make_multiplier(factor):
    """Outer function that returns a nested function."""

    def multiply(x):
        """Inner function that multiplies its argument by the outer function's variable."""
        return x * factor

    return multiply


# # Call the outer function with a factor of 3
multiply_by_3 = make_multiplier(3)
# # Call the inner function with an argument
result = multiply_by_3(10)
print(f"The result of multiplying 10 by 3 is: {result}")


# ================== Docstrings & Type Annotations ==================
# # Example 01:
def add(a: int, b: int) -> int:
    """Function to add two integers and return the result.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: Sum of a and b.
    """
    return a + b


# # Call the function
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# # Example 02:


def greet(name: str) -> None:
    """Function to greet a person with their name.

    Args:
        name (str): Name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}!")


# # Call the function
greet("Alice")
