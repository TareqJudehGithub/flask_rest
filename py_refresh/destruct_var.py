"""Destruct Variables"""


x = (5, 11)  # also works:  x = 5, 11


# destruct vars:
x, y = 5, 11


t = 1, 2
x, y = t

print(t, end="\n")


students_score = {"Emad": 96, "Amad": 88, "Tamer": 85}

print(list(students_score.items()))
# >>> returns a list of tuples


# now, lets destruct students and scores
for student, score in students_score.items():
  print(student, score)


print("\n")

people = [
  ("Emad", 41, "Designer"),
  ("Amjad", 47, "Developer"), 
  ("Yanal", 48,"Banker")
]

# 2nd person profission
print(people[1][2])

print("\n")

name, _, profession = people[0]
print(name, profession)

print("\n")
# all ages
for person in people:
  print(person[1])


print("\n")

# collecting all destructed values

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

print("\n")

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)