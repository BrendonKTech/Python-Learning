# Operators are symbols that perform operations on values or variables.

# Types of Operators:
# Arithmetic Operators (+, -, *, /, //, %, **)

# Comparison (Relational) Operators (==, !=, >, <, >=, <=)

# Logical Operators (and, or, not)

# Bitwise Operators (&, |, ^, ~, <<, >>)

# Assignment Operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)

# Identity Operators (is, is not)

# Membership Operators (in, not in)

# -----------------------------------------------------

# Arithmetic Operators
# Used to perform mathematical operations
a = 10
b = 3

print(a + b)  # Addition -> 13
print(a - b)  # Subtraction -> 7
print(a * b)  # Multiplication -> 30
print(a / b)  # Division -> 3.333...
print(a // b) # Floor Division -> 3
print(a % b)  # Modulus -> 1 (remainder)
print(a ** b) # Exponentiation -> 10³ = 1000

# -----------------------------------------------------

# Comparison Operators
# Used to compare values and return True or False.
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

# -----------------------------------------------------

# Logical Operators
# Used to combine conditional statements
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# -----------------------------------------------------

# Bitwise Operators
# These perform bitwise operations on numbers
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # Bitwise AND -> 1 (0001)
print(a | b)  # Bitwise OR -> 7 (0111)
print(a ^ b)  # Bitwise XOR -> 6 (0110)
print(~a)     # Bitwise NOT -> -6
print(a << 1) # Left Shift -> 10 (1010)
print(b >> 1) # Right Shift -> 1 (0001)

# -----------------------------------------------------

# Assignment Operators
# Used to assign values to variables
x = 5
x += 3  # x = x + 3 -> 8
x -= 2  # x = x - 2 -> 6
x *= 4  # x = x * 4 -> 24
x /= 3  # x = x / 3 -> 8.0
x %= 5  # x = x % 5 -> 3.0
x //= 2 # x = x // 2 -> 1.0
x **= 3 # x = x ** 3 -> 1.0

# -----------------------------------------------------

# Identity Operators
# Used to check if two objects refer to the same memory location
a = 10
b = 10
print(a is b)      # True (same memory location)
print(a is not b)  # False

# -----------------------------------------------------

# Membership Operators
# Used to check if a value is in a sequence
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)   # True
print("grape" not in fruits) # True
