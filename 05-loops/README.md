# **Loops in Python (Text Overview)**

## **1. Purpose of Loops**

Loops let you execute a block of code multiple times, automating repetitive tasks and iterating over collections of data without duplicating code.

## **2. Types of Loops**

- **For Loop**
  Iterates over each element of a sequence (like lists, tuples, strings, or ranges), executing the loop body once per element.
- **While Loop**
  Repeats as long as a given condition remains true; useful when the number of iterations isn’t known in advance.

## **3. Control Statements in Loops**

These statements alter the normal flow of a loop:

- **`continue`**
  Skips the rest of the current iteration and moves directly to the next.
- **`break`**
  Immediately terminates the loop, jumping to the first statement after it.
- **`else`** (on loops)
  A special clause that runs only if the loop completes all iterations without encountering a `break`.

## **4. Working with Lists and Indexing**

- Use a **for loop** to process each item in a list.
- **`enumerate()`** provides both the item and its index in one step.
- Manual indexing (using a separate counter variable) achieves the same but is more verbose.

## **5. Iterating Over Dictionaries**

- **Keys only**: A for loop over the dictionary yields its keys.
- **Key–value pairs**: Using the dictionary’s `items()` method returns each key together with its associated value.

## **6. Combining Loops and Control Statements**

By mixing `for`/`while` with `continue`, `break`, and `else`, you can:

- Skip specific iterations
- Exit early when a condition is met
- Detect and handle the “clean” completion of the loop

## **7. Best Practices**

1. **Prevent infinite loops**: Ensure your `while` conditions will eventually become false.
2. **Prefer `enumerate()`**: It cleanly handles index–item pairs.
3. **Use control statements judiciously**: `continue`, `break`, and `else` can make logic clearer—but overuse can reduce readability.
4. **Keep loop bodies concise**: Move complex logic into helper functions whenever possible.
5. **Test edge cases**: Try empty sequences or boundary values to verify correct behavior.

**In summary**, mastering loops—and the ways to control their execution—is essential for processing sequences and building efficient Python programs. Understanding `for` vs. `while`, using `continue`/`break`/`else`, and iterating over lists and dictionaries will equip you to handle virtually any repetition or traversal task in your code.
