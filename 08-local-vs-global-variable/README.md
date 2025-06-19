# **Local vs. Global Variables in Python**


## **1. Namespaces & Scopes (LEGB Rule)**

When Python looks up a name (variable or function), it searches in this order:

1. **L**ocal scope — names defined inside the current function.
2. **E**nclosing scope — names in any enclosing (outer) functions, for nested functions.
3. **G**lobal scope — names defined at the top level of the module.
4. **B**uilt‑in scope — names pre‑defined by Python (`len`, `print`, etc.).

---

## **2. Global Variables**

* **Definition**: Placed **outside** any function or class, at module level.
* **Accessibility**: Read‑only inside functions by default.
* **Modification**: To reassign a global name inside a function, you must use the `global` keyword.

**Pros & Cons**

* ✔️ Convenient for truly shared, constant values (e.g. configuration).
* ❌ Overuse leads to code that’s hard to debug and reason about, because any function can change state.

---

## **3. Local Variables**

* **Definition**: Declared **inside** a function (or block).
* **Scope**: Only visible and alive while that function is executing. After it returns, locals are discarded.
* **Shadowing**: A local name can hide (shadow) a global of the same name within its function.

---

## **4. Enclosing (Nonlocal) Variables**

* Occur in **nested functions**: an inner function can access names in its outer (enclosing) function.
* To **modify** an enclosing‐scope name (but not global), use the `nonlocal` keyword.


## **Code Examples**

```python
# === 1. Global vs. Local & Shadowing ===

x = 100  # Global variable

def shadow_example():
    x = 5   # This 'x' is local, and shadows the global 'x'
    print("Inside shadow_example, x =", x)

shadow_example()
print("Outside, global x =", x)
# --------------------------------------
# Output:
#   Inside shadow_example, x = 5
#   Outside, global x = 100



# === 2. Modifying a Global Variable ===

counter = 0  # Global

def increment():
    global counter     # Tell Python: use the global 'counter', not create a new local
    counter += 1

increment()
increment()
print("Global counter after increments:", counter)
# --------------------------------------
# Output:
#   Global counter after increments: 2



# === 3. Nested Functions & nonlocal ===

def outer():
    message = "Hello"

    def inner():
        nonlocal message    # Refers to 'message' in the enclosing 'outer' scope
        message += ", world!"
        print("Inside inner:", message)

    inner()
    print("Back in outer:", message)

outer()
# --------------------------------------
# Output:
#   Inside inner: Hello, world!
#   Back in outer: Hello, world!



# === 4. Name Resolution (LEGB) ===

var = "global"

def outer_scope():
    var = "enclosing"

    def inner_scope():
        var = "local"
        print("Inner sees:", var)     # picks local first
    inner_scope()
    print("Outer sees:", var)         # picks enclosing
outer_scope()
print("Module sees:", var)            # picks global

# --------------------------------------
# Output:
#   Inner sees: local
#   Outer sees: enclosing
#   Module sees: global
```

---

### Key Takeaways

* **Local** variables live and die inside functions; they don’t affect the module or other functions.
* **Global** variables exist for the entire runtime of the module and can be read anywhere, but to reassign you must declare them `global`.
* **Enclosing** (nonlocal) variables let nested functions share state without touching globals.
* Understanding the **LEGB** lookup order helps predict exactly which variable a given name refers to.
