"""
**kwargs collects all keyword arguments and puts it into a dict.
  dict[key] is the keyword argument
"""


def named(**kwargs):
  print(kwargs)

  # print firstname keyword
  return "Hello, {}".format(kwargs["firstname"]).title()


print(named(firstname="John", lastname="Smith"))

print("\n")

def print_nicely(**kwargs):
  
  # print both key (keyword argument) and value
  print(kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")


print_nicely(firstname="John", lastname="Smith")

