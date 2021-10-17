grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for  mark in grades:
  total += mark

avg_grade = total / amount

print(avg_grade)


# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
  if  number % 2 == 0:
    evens.append(number)


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ").lower()
if user_input == 'q':
  print("Quit")
if user_input == "a":
  print("Add")
