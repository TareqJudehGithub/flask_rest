"""
List comprehensions
"""

numbers = [1, 3, 5]
doubled = list()

# for loop
for i in numbers:
  doubled.append(i * 2) 
print(doubled)


# using list comprehensions
doubled_v2 = [x * 2 for x in numbers]
print(doubled_v2)


print("\n")

# add names starting with an 'S' to starts_s list

friends = ["Rolf", "Same", "Samantha", "Saurabh", "Jen"]
starts_s = list()

# for loop
for name in friends:
  if name.startswith("S"):
    starts_s.append(name)

print(starts_s)

# list comp
starts_s_vs = [name for name in friends if name.startswith("S")]

print(starts_s_vs)
