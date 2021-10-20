"""
Magic Methods
 - Methods with two __ in Python are called magic methods.
 - It's called magic methods because you don't have to call it manually, Python
   will call it for you.
 - To call a magic method, we just instantiate an object and call it, without
   including any methods.

  List of magic methods:
    __str__(self)
     - __str__ method is called for us when we need to turn an obj (bob) into 
       a string.
     - __str__ is meant to be shown for users.

      def __str__(self):
      return f"Hello! {self.name}! You're {self.age} years old."


    __repr__(self)
      - __repr__ returns a string that allows us to recreate the obj (bob) very
      easily.
      - __repr__ magic method is used for testing and debuging, and is not meant
      to be shown for the users.
      - * MAKE SURE to comment any __str_ method before testing out the __repr__
        method, or it won't be displayed.

"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # methods
  # def __str__(self):
  #   return f"Hello! {self.name}! You're {self.age} years old."
  
  def __repr__(self):
    return f"<Person('{self.name}' {self.age})>"

# instantiate a bob obj from class Person
bob = Person("Bob", 35)
print(bob)
