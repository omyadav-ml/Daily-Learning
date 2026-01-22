# class Two_D_vector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
        
    
# class Three_D_vector:
#     def __init__(self,i,j,k):
#         super().__init__(self,i,j)
#         self.k=k

# a=Two_D_vector(1,2)
# b=Three_D_vector(1,2,3)
#q1.]
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()

# Q2]

class Animals():
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhow Bhow!")

Dog.bark()

# Q3]
class Employee:
    def sal(self, salary, increment):
        self.salary = salary
        self.increment = increment
        print(f"The salary is {salary} and increment is {increment}")

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment / 100)

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if value < 0:
            print("Increment cannot be negative!")
        else:
            self._increment = value


# usage
e = Employee()
e.sal(120000, 20)
print(e.salaryAfterIncrement)  
e.increment = 10             
print(e.salaryAfterIncrement) 

# Q4]
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = Complex(3, 2)
c2 = Complex(1, 7)
c3 = c1 + c2   
print(c3)    


import random

class Dice:
    def roll(self):
        a=(1,2,3,4,5,6)
        b=(1,2,3,4,5,6)
        m=random.choice(a)
        n=random.choice(b)
        print(f" {m},{n}")

om=Dice()
om.roll()


class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount

    def show_balance(self):
        print("Balance",self.balance)    

acc=BankAccount("Om",1000)
acc.deposit(500)
acc.show_balance()    