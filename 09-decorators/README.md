# **Decorators in Python:**

## **1. What Are Decorators?**

A **decorator** is a callable that takes a function (or method) as input, wraps it in additional functionality, and returns a new function. Crucially, the original function’s code remains untouched—decorators “decorate” it from the outside.

## **2. How They Work:**

1. **Function as First-Class Citizen**

   - In Python, functions can be passed around like variables.

2. **Wrapper Function**

   - The decorator defines an inner function (the **wrapper**) that:

     - Executes code **before** calling the original function.
     - Calls the original function.
     - Executes code **after** the original function returns.

3. **Syntactic Sugar (`@`)**

   - Placing `@decorator_name` above a function is equivalent to:

     ```python
     def func(...):
         ...
     func = decorator_name(func)
     ```

## **3. Types of Decorators**

1. **Simple Function Decorators**

   - No parameters; directly wrap the target function.

2. **Parameterized Decorators**

   - Accept arguments themselves (e.g., `@retry(max_attempts=3)`).
   - Implemented via a decorator factory that returns the real decorator.

3. **Class-Based Decorators**

   - Encapsulate state in an object with a `__call__` method.

4. **Built-in Decorators**

   - Provided by Python for common patterns:

     - `@staticmethod`, `@classmethod`
     - `@property`

## **4. Key Use Cases**

- **Logging:** Track when functions start, finish, or fail.
- **Authentication & Authorization:** Enforce access control before running sensitive code.
- **Timing & Performance Monitoring:** Measure execution time for profiling.
- **Caching / Memoization:** Store and reuse results of expensive calls.
- **Retry Logic:** Automatically retry transient failures (e.g., network requests).
- **Input Validation:** Sanitize or validate arguments before core logic runs.

## **5. Code Example**

```python
import functools, time, logging

logging.basicConfig(level=logging.INFO)

def log_and_time(fn):
    """Decorator that logs calls and measures execution time."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {fn.__name__} with {args} {kwargs}")
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = (time.time() - start) * 1000  # ms
        logging.info(f"{fn.__name__} completed in {elapsed:.1f}ms")
        return result
    return wrapper

@log_and_time
def compute_sum(n):
    """Return the sum of numbers from 0 to n-1."""
    return sum(range(n))

# Usage
total = compute_sum(100_000)
```

**What Happens:**

- When `compute_sum` is called, `log_and_time`’s wrapper logs the call, times execution, logs the duration, then returns the original function’s result.

## **6. Benefits of Using Decorators**

- **Separation of Concerns:** Keeps auxiliary logic (logging, timing, security) out of your core function.
- **Reusability:** Write the decorator once and apply it to many functions.
- **Readability:** A single `@decorator` line clearly indicates added behavior, rather than scattering similar code across multiple functions.
- **Maintainability:** Changes to the shared behavior live in one place, reducing the risk of inconsistencies.
- **Flexibility:** Enable or disable cross-cutting features by simply adding or removing decorators.

By mastering decorators, you gain a powerful tool for writing clean, modular, and maintainable Python code—letting you “wrap” extra functionality around your functions with minimal effort.
