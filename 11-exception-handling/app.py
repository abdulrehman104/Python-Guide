# —————— Basic tryexcept Structure ————————————————————————————————

try:
    # Code that might raise an exception
    result = 10 / int(input("Enter divisor: "))
    print("Result is", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# —————— Handling Multiple Exceptions ————————————————————————————————
try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result is", y)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input; please enter an integer.")


# —————— Handling Generic Exceptions ————————————————————————————————
try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result is", y)
except Exception as e:
    print(f"An error occurred: {e}")


# —————— Using the finally Block ————————————————————————————————
try:
    file = open("data.txt")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    # Always runs, whether an exception occurred or not
    file.close()
    print("File closed.")
