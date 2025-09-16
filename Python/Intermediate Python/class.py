"""
# class student:
#     name = "raj"
# s1 = student()
# print(s1.name)

# s2=student()
# print(s2.name) 


It is class
class car:
    color='blue'
    brand="Tesla"  

    def __init__(self,color,brand): #the __init__ is dunder method which is automatically called when object is created
        self.color=color
        self.brand=brand
        print("I created an object")

car2=  car('blue','brand')
car2.color="Red" #this is instance attribute. object attribute  preferfed over class attribute 
print(car2.color,car2.brand)

"""
class Employee:
    Skills="Python"
    salary=120000

    def getInfo(self):
        print(f"The skills required are {self.Skills}. The salary is {self.salary }")
    def greet(self):
        print("Good Morning")
        
om=Employee()
om.name="Om"
print(om.name,om.salary)
om.greet()
om.salary=119999
om.getInfo()

# Q1.]
class Programmer:
    company="Google"
    def __init__(self,name,salary,location):
        self.name=name
        self.salary=salary
        self.location=location

a=Programmer("Om",120000,"Mumbai")
print(a.name,a.salary,a.location,a.company)
b=Programmer("Rahul",110000,"Pune")
print(b.name,b.salary,b.location,b.company)

# Q2.]
class calculator:
    def __init__(self,n):
        self.n=n       
    def square(self):
        print(f"The square is : {self.n**2}")  

    def cube(self):
        print(f"The square is : {self.n**3}")

    def squareroot(self):
        print(f"The square is : {self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello Om")        


number=int(input("Enter a number: "))
a=calculator(number)
a.greet()
a.square()
a.cube()
a.squareroot()
print("Hello Om")            


# Q3.]
from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def book(slf,fro,to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf,fro,to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(200,5000)}")

t=Train(245)
t.book("Varanasi","Mumbai")
t.getStatus()
t.getFare("Varanasi","Mumbai")