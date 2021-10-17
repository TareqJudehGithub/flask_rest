"""
lambda functions are functions without a name.
lambda are meant to be short functions.

lambda x, y: x + y
lambda inputs: output


lambda x, y: x + y

In Python, list comprehension is recommended, unless python is used along side
a language like Javascript for example.
"""


sequence = [1, 3, 5, 9]

# double the sequence

# list comprehensions
doubled_seq = [i * 2 for i in sequence]
print(doubled_seq, end="\n")

# map
def double_val(x):
  return x * 2

doubled_map = list(map(double_val, sequence))
print(doubled_map)

# lambda:
double_lamb = list(map(lambda x: x * 2, sequence))
print(double_lamb)