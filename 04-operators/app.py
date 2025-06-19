# ================= Addition Operators =================
print("================= Addition Operators =================")

a = 5 + 3
print("5 + 3 =", a)

# Subtraction
b = 10 - 4
print("10 - 4 =", b)

# Multiplication
c = 7 * 2
print("7 * 2 =", c)

# Division
d = 9 / 2
print("9 / 2 =", d)

# Floor Division
e = 9 // 2
print("9 // 2 =", e)

# Modulus
f = 9 % 2
print("9 % 2 =", f)

# Exponentiation
g = 3 ** 4
print("3 ** 4 =", g)

# Unary Plus/Minus
h = +5
print("+5 =", h)
i = -a
print(f"-({a}) =", i)



# ================= Assignment Operators =================
print("================= Assignment Operators =================")
# Simple Assignment
x = 10
print("x =", x)

# Add AND assignment
a = 5
a += 3
print("a += 3 ->", a)

# Subtract AND assignment
b = 10
b -= 4
print("b -= 4 ->", b)

# Multiply AND assignment
c = 7
c *= 2
print("c *= 2 ->", c)

# Divide AND assignment
d = 9
d /= 2
print("d /= 2 ->", d)

# Floor Divide AND assignment
e = 9
e //= 2
print("e //= 2 ->", e)

# Modulus AND assignment
f = 9
f %= 2
print("f %= 2 ->", f)

# Exponent AND assignment
g = 3
g **= 4
print("g **= 4 ->", g)

# Bitwise AND assignment
h = 6  # 0b110
h &= 3  # 0b011
print("h &= 3 ->", h)

# Bitwise OR assignment
i = 6  # 0b110
i |= 3  # 0b011
print("i |= 3 ->", i)

# Bitwise XOR assignment
j = 6  # 0b110
j ^= 3  # 0b011
print("j ^= 3 ->", j)

# Right shift AND assignment
k = 8  # 0b1000
k >>= 2
print("k >>= 2 ->", k)

# Left shift AND assignment
l = 2  # 0b0010
l <<= 3
print("l <<= 3 ->", l)


# ================= Comparison Operators =================
print("================= Comparison Operators =================")
# Equal
print("5 == 3 ->", 5 == 3)

# Not equal
print("5 != 3 ->", 5 != 3)

# Greater than
print("5 > 3 ->", 5 > 3)

# Less than
print("5 < 3 ->", 5 < 3)

# Greater than or equal to
print("5 >= 3 ->", 5 >= 3)

# Less than or equal to
print("5 <= 3 ->", 5 <= 3)

# Identity (same object)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b ->", a is b)
print("a is c ->", a is c)

# Not identity
print("a is not c ->", a is not c)

# Membership (in)
print("2 in a ->", 2 in a)

# Not membership
print("4 not in a ->", 4 not in a)


# ================= Logical Operators =================
print("================= Logical Operators =================")

# Logical AND
x = True
y = False
print("True and False ->", x and y)
print("(5 > 3) and (2 < 4) ->", (5 > 3) and (2 < 4))

# Logical OR
print("True or False ->", x or y)
print("(5 > 3) or (2 > 4) ->", (5 > 3) or (2 > 4))

# Logical NOT
print("not True ->", not x)
print("not (5 > 3) ->", not (5 > 3))
