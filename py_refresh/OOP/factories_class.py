#factories_class.py

class  Book:
  TYPES = ("hardcover", "paperback")

  def __init__(self, name, type, weight):
    self.name = name.title()
    self.type = type.capitalize()
    self.weight = weight

  def __repr__(self):
    return f"<Book(Book title:{self.name}\nBook type:{self.type}\nBook weight: \
    {self.weight}g.)>"
  
  @classmethod
  # adding 100 because hardcover weights heavier than paperback
  def hardcover(cls, name, weight):
    print("\n")
    return cls(name, cls.TYPES[0], weight + 200) 
  
  @classmethod
  def paperback(cls, name, weight):
    print("\n")
    return cls(name, cls.TYPES[1], weight + 200) 


# accesssing Typles tuple inside class Book
Book.TYPES


# Creating an instance of Book class

book_1 = Book("harry potter", "hardcover", 1500)

# pass "harry potter" value as a param for name object, then it will be assigned
# to the name property of the self object (which is an empty container at this
# stage), and finally it will be printed using print(book_1.name)

print(book_1, end="\n")


# Now because we created a class method inside the class, we no longer need to
# create any new objects first, all we need to do now is  call the class method
# we created:

book_hardcover = Book.hardcover("harry potter", 1700)
print(book_hardcover)

book_paperback = Book.paperback(" The hobbit", 700)
print(book_paperback)
