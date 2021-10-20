""" 
class methods vs static methods
 
 Instance methods
  - Instance methods require no initialization (__init__)
  - Instance methods uses the self parameter.
  - Instance methods get self as an object (instance) in them.
  - When calling instance methods we need an instance (new object).
  - We can call instance methods by using its function with the class.
  - Instance methods are used when we want to produce an action that uses the data
    inside the instance created (self, name, age) for creating new instances or
    for modifying it.
  
 Class methods
  - Class methods require no initialization (__init__)
  - A class methods must me preceded with  decorator @classmethod
  - Class methods uses the cls parameter.
  - cls parameter in a class method will be the class it self (cls is a 
    reference to the class it self).
  - Class methods, when being called does not need an instance; because when the
    we added @classmethod, Python will automatically for us add cls as the method
    parameter (see the example below when calling the class method).
  - Class methods are often used as factories. For more on factories, see file 
    factories_class.py

 Static methods
  - Static methods doesn't have any information about the class or the instance
    (self), it's just it's own separate function inside the class.
  - Static methods require no initialization (__init__)
  - A static methods must me preceded with  decorator @staticmethod
  - Unlike instance and class methods, static methods doesn't have a parameter,
    static methods doesn't have anything in them.
  - We call static methods by calling the class first followed by the method. 
  - Static methods are just used to placing methods/functions inside a class.



"""

class ClassTest:

  # type 1: instance method
  def instance_method(self):
    print("Display me in your terminal")
    return f"Calling instance method: {self}"

  # type 2 class method:
  @classmethod
  def class_method(cls):
    print("Calling class method {}".format(cls)) 

  @staticmethod
  def static_method():
    print("Calling static_method")



# calling instance method - instance methods needs the object (instance_method
# in our example) to call them:

# calling instance method: option 1
option_1 = ClassTest().instance_method()
print(option_1) 

print("\n")

# calling instance method: option 2
# ClassTest.instance_method(option_1)

# calling a class method
ClassTest.class_method()

# calling a static method
ClassTest.static_method()


# 