"""
Python refresher
"""

# variables  

# swap a and v variable values
a = 25  # assignment expression
b = 50

print(a, b)

c = a
a = b
b = c

print(a, b)

# round using f string and format func
weight = float(input("Enter your weight: "))
print(f"Your weight is: {weight: .2f}")

print(format(10.541546, '.2f'))

print(type(('hi')))