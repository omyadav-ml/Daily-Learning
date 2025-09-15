# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()

# # 1. This is an example of multilevel inheritance
class Employee:
  a=3

class Manager(Employee):
  b=4

class Boss(Manager):
  c=5

e=Employee()
print(e.a) #prints 3 

r=Manager()
print(r.a,r.b)

t=Boss()
print(t.a,t.b,t.c)


# Super init  Calls constructor of the base class 
class Employee:
  def __init__(self):
    print("Constructor of Employee")
  a=3

class Manager(Employee):
  def __init__(self):
     super().__init__()
     print("Constructor of Manager")
  b=4

class Boss(Manager):
  def __init__(self):
    super().__init__() #Calls Manager Constructor
    print("Constructor of Boss")
  c=5

t=Boss()
print(t.a,t.b,t.c)

# class method

class student:
  a=1

  @classmethod
  def ran(cls):
    print(f"The class attribute of a is {cls.a}")

b=student()
e.a=12
b.ran()

# property method

class student:
    a = 1  # class attribute

    @property
    def ran(self):
        return f"The class attribute of a is {self.a}"

b = student()
print(b.ran)



