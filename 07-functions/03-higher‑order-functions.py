# ================== map(func, iterable) ==================

# Example 01:
"""Applies func to each item and returns an iterator of results."""

nums: list = [1, 2, 3, 4, 5]
squares: list = map(lambda x: x*x, nums)
print(list(squares))  # [1, 4, 9, 16, 25]

# # Example 02:


def square(x: int) -> int:
    return x * x


nums: list = [1, 2, 3, 4, 5]
squares: list = map(square, nums)
print(list(squares))  # [1, 4, 9, 16, 25]


# ================== filter(func, iterable) ==================
"""Keeps only items for which func(item) is True."""

# Example 01:
nums: list = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4]

# Example 02:
def is_even(x: int) -> bool:
    return x % 2 == 0

nums: list = [1, 2, 3, 4, 5]
evens = filter(is_even, nums)
print(list(evens))  # [2, 4]



# ================== functools.reduce(func, iterable[, initializer]) ==================
"""Accumulates a result by applying func cumulatively."""

from functools import reduce

# Example 01:
# Compute product of all numbers
nums = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, nums)
print(product)  # 24


# Example 02:
def multiply(a: int, b: int) -> int:
    return a * b    

nums = [1, 2, 3, 4]
product = reduce(multiply, nums)
print(product)  # 24



# ================== sorted(iterable, *, key=None, reverse=False) ==================
"""Returns a new sorted list; key is itself a function applied to each element for comparison."""

# Sort by absolute value, descending
nums = [-3, 1, -2, 4]
print(sorted(nums, key=abs, reverse=True))  # [-3, 4, -2, 1]



# ================== zip(*iterables) ==================
"""Aggregates items from multiple iterables into tuples. Often used with unpacking and mapping."""

names = ["Ali", "Sara", "Tom"]
scores = [88, 92, 75]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Ali: 88
# Sara: 92
# Tom: 75



# ================== enumerate(iterable, start=0) ==================
"""Wraps an iterable and returns pairs (index, item)."""

colors = ["red", "green", "blue"]
for idx, color in enumerate(colors, start=1):
    print(idx, color)
# 1 red
# 2 green
# 3 blue



# ================== any(iterable) / all(iterable) ==================
"""
any: True if any element is truthy.
all: True if all elements are truthy.
"""
flags = [True, False, True]
print(any(flags))  # True
print(all(flags))  # False



# ================== max(iterable, *, key=None) / min(iterable, *, key=None) ==================
"""Take an optional key function to determine comparison value."""
words = ["apple", "banana", "cherry"]
# Longest word by length
print(max(words, key=len))  # "banana"
