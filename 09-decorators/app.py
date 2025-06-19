import time
import functools

# ———————————————————————————————— A simple decorator function ————————————————————————————————

def decorator(func):
    """A simple decorator that wraps a function to add behavior before and after its execution."""
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function


@decorator
def greet():
    print("Hello, World!")


greet()


# ————————————————————————————————  Basic Example: Simple Logging Decorator ————————————————————————————————


def log_call(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper


@log_call
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# ———————————————————————————————— Advance Example: Parameterized Decorator for Timing ————————————————————————————————


def timer(unit: str = "ms"):
    """Decorator factory: unit can be 'ms' or 's'."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = fn(*args, **kwargs)
            elapsed = time.time() - start
            if unit == "ms":
                elapsed *= 1000
                print(f"[TIMER] {fn.__name__} took {elapsed:.2f} ms")
            else:
                print(f"[TIMER] {fn.__name__} took {elapsed:.4f} s")
            return result
        return wrapper
    return decorator


@timer("s")
def compute(n):
    time.sleep(1)
    return sum(i*i for i in range(n))


compute(100_000)
