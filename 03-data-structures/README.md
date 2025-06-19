# **Data Structures in Python (Text Overview)**

## **1. Lists**

- **Definition:** Ordered, mutable collections of items.
- **Syntax:** Defined with square brackets, e.g. `[10, 20, 30]`.
- **Key Characteristics:**

  - Allow duplicate elements.
  - Support indexing (`lst[0]`) and slicing (`lst[1:3]`).
  - Mutable: you can append, insert, remove, or reassign elements.

- **Common Operations:**

  - `append()` to add at the end.
  - `insert()` to add at an arbitrary position.
  - `pop()` or `remove()` to delete elements.
  - Iteration with `for`, often using `enumerate()` when you need indices.

- **Use When:** You need an ordered, changeable sequence of items.

## **2. Tuples**

- **Definition:** Ordered, immutable collections of items.
- **Syntax:** Defined with parentheses (or even without), e.g. `(“Bob”, 30, “Engineer”)`.
- **Key Characteristics:**

  - Allow duplicate elements.
  - Support indexing and slicing like lists.
  - Immutable: once created, you cannot add, remove, or change elements.
  - Can be unpacked directly into variables.

- **Common Operations:**

  - Indexing (`tpl[1]`) and slicing (`tpl[:2]`).
  - Unpacking: `name, age, role = tpl`.

- **Use When:** You need a fixed collection of items that shouldn’t change (e.g., coordinates, fixed configuration).

## **3. Dictionaries**

- **Definition:** Unordered (as of Python 3.7 they preserve insertion order), mutable mappings from **unique** keys to values.
- **Syntax:** Defined with curly braces, e.g. `{"name": "John", "age": 30}`.
- **Key Characteristics:**

  - Keys must be hashable (e.g., strings, numbers, tuples).
  - Values can be any type and duplicated.
  - Fast lookup, insertion, and deletion by key.

- **Common Operations:**

  - Access: `d[key]` or `d.get(key, default)` (safer when key might be missing).
  - Add/update: `d[new_key] = value`.
  - Remove: `del d[key]` or `d.pop(key)`.
  - Membership: `key in d`.
  - Iteration over keys (`for k in d`), values (`d.values()`), or items (`d.items()`).

- **Use When:** You need to associate unique identifiers (keys) with values for fast lookup.

## **4. Strings**

- **Definition:** Immutable sequences of Unicode characters.
- **Syntax:** Enclosed in single, double, or triple quotes, e.g. `"Hello"`.
- **Key Characteristics:**

  - Support indexing and slicing like lists/tuples.
  - Immutable: any “modification” returns a new string.
  - Rich built‑in methods for searching, splitting, replacing, and formatting.

- **Common Operations:**

  - Concatenation (`+`) and repetition (`*`).
  - Slicing (`s[1:4]`) and indexing (`s[0]`).
  - f‑strings (`f"Name: {name}"`) for interpolation.
  - Methods like `.upper()`, `.split()`, `.replace()`, `.strip()`.

- **Use When:** You need to represent and manipulate textual data.

## **5. Sets (Bonus)**

- **Definition:** Unordered, mutable collections of **unique** elements.
- **Syntax:** Defined with curly braces or `set()` constructor, e.g. `{1, 2, 3}`.
- **Key Characteristics:**

  - No duplicate elements.
  - No indexing or slicing (because order is not guaranteed).
  - Support mathematical set operations: union, intersection, difference.

- **Common Operations:**

  - Add/remove: `s.add(x)`, `s.remove(x)`.
  - Membership: `x in s`.
  - Set algebra: `s1 & s2`, `s1 | s2`, `s1 - s2`.

- **Use When:** You need to enforce uniqueness, perform fast membership tests, or use set‑algebra operations.

## **6. Choosing the Right Structure**

- **Lists** for ordered, changeable sequences.
- **Tuples** for fixed, unchangeable sequences.
- **Dictionaries** for key‑value mappings and fast lookup by key.
- **Strings** for textual data.
- **Sets** for unique collections and membership testing.

**Best Practices:**

1. **Use the most specialized type** that fits your needs (immutability when possible).
2. **Leverage built‑in methods** rather than manual loops for common patterns (e.g., `.append()`, `.get()`, `.split()`).
3. **Understand performance characteristics:** lists and dictionaries have different time complexities for insertion, deletion, and lookup.
4. **Keep data structures simple and expressive:** combine them (e.g., list of dicts) only when it clearly models your data.
