#-----------------------------------------------------------------------------
# Name:        Math Functions (math_functions.py)
# Purpose:     Demonstrating min, max, round, abs, pow and functions from the
#              math module
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     28-Sept-2026
#-----------------------------------------------------------------------------

# import the module first, at the top of the program
import math

# --- Built-in functions ------------------------------------------------------
# minimum value
minimum = min(2, 5, 8, -3, 14)
print(minimum)

# maximum value
maximum = max(2, 5, 8, -3, 14)
print(maximum)

# rounding to a certain number of decimal places
rounded_value = round(5.669564564)
print(rounded_value)

# absolute value (distance from zero)
negative_integer = -10
positive_value = abs(negative_integer)
print(positive_value)

# power
power = pow(4, 3)
print(power)


# --- The math module ---------------------------------------------------------
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
