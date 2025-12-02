# An object is a collection of data (variables) and methods (functions) that act on the data.
# A class is a blueprint for creating objects. It defines a set of attributes and methods that
# There are 2 types of objects in Python:
# 1. Instance Object: An instance object is created from a class. It is an instance of the class.
# 2. Class Object: A class object is created when the class is defined. It is an instance of the type 'type'.

# One class can have only one class object, but can have multiple instance objects.
# A class object can represented by using the class name(ex. class ClassName, so here ClassName in the code represents the class object).
# An instance object is represented by using the instance name(ex. obj = ClassName(), so here obj represents the instance object).

# A class object is created when the class is defined, and an instance object is created by this:   obj = ClassName().


class Test:
    x = 5  # Class attribute
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f1(self):
        print("This is an instance method of class Test")
        # Instance method can access instance attributes using self, and does tasks related to instance object.

    @staticmethod
    def f2():
        print("This is a static method of class Test")
    
    @classmethod
    def f3(cls):
        print("This is a class method of class Test")
        print(cls.x)  # Accessing class attribute using cls



t1 = Test(5, 10)  # Creating an instance object t1 of class Test
t2 = Test(15, 20)  # Creating another instance object t2 of class Test
print(t1.a, t1.b)  # Accessing attributes of instance object t1
print(t2.a, t2.b)  # Accessing attributes of instance object t2
Test.f3()  # Calling class method using class object
Test.f2()  # Calling static method using class object