import operator as op
from functools import reduce

def multiply(*args): # collect all positional arguments
  print(args)

multiply(1, 2, 3, 4)


def addition(x, y):
  return x + y


nums ={"x": 15, "y": 20}

print(addition(**nums))  



print("\n")

# calculator

def calculator(*args, operator):
  if operator == "+":
  
    return sum(args)
  
  elif operator == "-":
    result = reduce(op.__sub__, args)
    return result
  
  elif operator == "*":
    result = reduce(op.__mul__, args)
    return result

    # or using for loop
    total = 1
    for i in args:
      total *= i
    return total

  else:
    
    result = reduce(op.__truediv__, args)
    return result


print(calculator(50, 10, 2, operator="/"))