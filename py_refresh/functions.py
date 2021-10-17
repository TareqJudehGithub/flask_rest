"""
Functions

"""

# declare function
def hello():              # function header
  return "Hello, world!"  # function header

# call function

print(hello())

print("\n")


def user_age_in_seconds():
  user_age = int(input("Enter your age: "))
  age_seconds = user_age * 365 * 24 * 60 * 60 * 60
  return age_seconds


print(user_age_in_seconds())


def fullname(first, last): # params
  return first + last


print(fullname("Tareq", "Judeh")) # positional arguments


def fullname(first, last): # 
  return first + last


print(fullname(first="Tareq", last="Judeh")) # keyword arguments

"""
positional arguments always go first
It is recommended to use keyword arguments
"""

# default parameters

def addition(x, y=15):
  return x + y

print(10) # x = 10by default, y=15

print("\n")

# =======================================
# Complete the function by making sure it returns 42. .
def return_42():
    # Complete function here
    # 'pass' just means "do nothing". Make sure to delete this!
    return 42
# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.
print(return_42())