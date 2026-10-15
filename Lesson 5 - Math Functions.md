# Lesson 5 - Math Functions

The example code for this lesson is in `math_functions.py`. Open it alongside
these notes and run it as we go.

We already know how to do math operations in Python. This lesson adds some
built-in math functions we can use.

## Built-in functions

| Function | Returns |
|---|---|
| `min(a, b, c, ...)` | the smallest value |
| `max(a, b, c, ...)` | the largest value |
| `round(x, decimals)` | `x` rounded to `decimals` places (default 0) |
| `abs(x)` | the absolute value (distance from zero) |
| `pow(x, y)` | `x` to the power of `y` |

```python
# minimum value
minimum = min(2, 5, 8, -3, 14)
print(minimum)

# maximum value
maximum = max(2, 5, 8, -3, 14)
print(maximum)

# rounding to a certain number of decimal places
rounded_value = round(5.664564564, 2)
print(rounded_value)

# absolute value (distance from zero)
negative_integer = -10
positive_value = abs(negative_integer)
print(positive_value)

# power
power = pow(4, 3)
print(power)
```

## The math module

A module provides extra functions we can use. We import the module at the top
of the program (so it can be used everywhere), then use its functions.

```python
# import the module first
import math

# rounding up and down
num = math.ceil(5.2)
print(num)

num = math.floor(5.8)
print(num)

# hypotenuse
hypotenuse = round(math.hypot(5, 8), 2)
print(hypotenuse)

# greatest common divisor
greatest_common_divisor = math.gcd(18, 24)
print(greatest_common_divisor)

# square root
print(math.sqrt(49))
```

There are many more math functions: https://www.w3schools.com/python/module_math.asp

## Lab

That is it for the lesson. Move on to Lab 5, in `README.md`.
