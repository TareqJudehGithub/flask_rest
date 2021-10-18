"""
OOP

Python creates a new container (instantiate a new obj), and calls  __init__ 
method, and it will create self, modifying attributes inside self (like 
self.name)

"""

class  Student:
  def __init__(self, name, grades):         # method
    self.name = name        # attributes
    self.grades = grades

  def avg_grades(self):
    # return round(sum(self.grades) / len(self.grades), ndigits=2)
    # return f"{sum(self.grades) / len(self.grades):.2f}"
    return "{:.2f}".format(sum(self.grades) / len(self.grades))



# instantiate a new obj from class Student
student_1 = Student("Rolf", (90, 88, 91))

print(student_1.name)    # // "Rolf"
print(student_1.grades)  # // (90, 88, 91)
print(student_1.avg_grades())

print("\n")
# instantiate student_2
student_2 = Student("Bob", (84, 93, 100))
print(student_2.name)
print(student_2.grades)
print(student_2.avg_grades())

