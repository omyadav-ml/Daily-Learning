import module
"""
#This is match statement note a case statement cuz in python does not have case statement
def week(num):
    match num:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid week number"
        
num=int(input("Enter the num of week:"))
print(week(num))

#Merge statement

dict1={'Babbu':'Yadav','Om':'Mishra'}
dict2={'Aryan':'Yadav','Aryaan':'Mishra'}
merged =dict1 | dict2
print(merged)


price=int(input("Enter the amount:"))
txt=f"It is very {'Expensive' if price>50 else "cheap"}"
print(txt)

#Exception Handling
#finally will run even it is error finally runs 
def main():

    try:
        a=int(input("Hey,Enter a number:"))
        print(a)
    except Exception as e:
        print(e)
    finally:
        print("Hey I a, inside of finally")

main()

# try/except

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# raise
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    print("Access granted")

check_age(16)


#module
from module import myfun


# Global key world
a=98

def fun():
    global a
    a=3
    print(a)


print(a)
fun()
"""
# Enumerate Function
list=[23,44,56,76,88]
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function
for index, item in enumerate(list):
    print(f"The item at index {index} is {item}")

# list comprehansion
 
def square(x):
    return x**2

nums = [1, 2, 3, 4]
squared_nums = [square(x) for x in nums]
print(squared_nums)

# zip
names=["om","aryan"]
roll_no=[29,30]
for name,roll in zip(names,roll_no):
    print(name,roll)
