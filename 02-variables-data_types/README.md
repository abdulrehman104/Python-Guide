# **Variables & Data Types in Python (Text Overview)**

## **1. What Is a Variable?**

- **Definition:** A variable is a named container that holds data during program execution.
- **Purpose:** It gives a meaningful name to values so you can store, retrieve, and manipulate information easily.

## **2. Variable Naming Rules**

1. **Start with a letter or underscore** (`a–z`, `A–Z`, `_`).
2. **Cannot start with a digit** (`0–9`).
3. **Only letters, digits, and underscores** allowed—no spaces or special characters.
4. **Case‑sensitive:** `Age`, `age`, and `AGE` are three distinct names.
5. **Avoid Python keywords:** Words like `if`, `for`, `print`, etc., cannot be used as variable names.
6. **Choose descriptive names** to clarify the variable’s role (e.g., `student_name` rather than `sn`).

## **3. Naming Conventions**

- **Snake Case:** All lowercase with underscores between words (preferred in Python).
- **Camel Case:** Lowercase first word, subsequent words capitalized (common in other languages).
- **Pascal Case:** Every word capitalized, no separators (often used for class names).

## **4. Initializing Variables**

- Use the assignment operator (`=`) to bind a name to a value.
- A variable comes into existence at its first assignment and can change (“vary”) over time.

## **5. Core Data Types**

1. **Integer (`int`):** Whole numbers without a fractional part (e.g., `42`, `-7`).
2. **Floating‑Point (`float`):** Decimal numbers (e.g., `3.14`, `-0.001`).
3. **String (`str`):** Sequences of characters enclosed in quotes (e.g., `"hello"`, `'Python3'`).
4. **Boolean (`bool`):** Logical values `True` or `False`, used in conditionals and logic tests.

## **6. How Python Treats Data Types**

- **Dynamic Typing:** You do not declare a variable’s type; it’s determined at runtime from the assigned value.
- **Type Conversion:** You can convert between types (e.g., from `int` to `str`), but only in ways that make sense for the data.

## **7. Best Practices**

1. **Consistent Naming:** Stick to one convention (ideally snake case) across your project.
2. **Meaningful Names:** Select names that describe the data’s purpose (e.g., `total_price` instead of `tp`).
3. **Avoid Global State:** Limit use of global variables to truly shared, constant configuration values.
4. **Document with Comments:** When a variable’s role is non‑obvious, add a brief comment explaining its use.
5. **Validate Inputs:** When taking user‑provided or external data, ensure it matches the expected type before use.

## **8. Why This Matters**

Understanding how to name and use variables, and knowing Python’s core data types, is foundational for writing clear, correct, and maintainable code. These principles allow you to:

- **Communicate intent** to other developers (and your future self).
- **Prevent bugs** related to naming collisions or unexpected types.
- **Build complex programs** by combining simple, well‑typed building blocks.

Mastering variables and data types paves the way for deeper Python concepts—functions, data structures, object orientation, and beyond.
