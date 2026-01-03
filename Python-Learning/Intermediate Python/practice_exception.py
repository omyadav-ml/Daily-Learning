# Q1.]
try:
    with open ("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open ("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open ("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank You")

# Q2.]
num=[1,2,3,4,5,6,7,8]
for i,item in enumerate(num):
    if i == 2 or i == 4 or i == 6:
        print(item)

# Q3.]
num=int(input("Enter the number to evaluate table:"))
table=[num*i for i in range(1,11)]
print(table)

# Q4.]

def month(num):
    match num:
        case 1:
            return "January"
        case 2:
            return "Feburay"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return("Invalid month")
num=int(input("Enter the month name: "))
print(month(num))

# Q5.]
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merge= dict1 | dict2
print(merge)

# Q6.]
x = [1, 2, 3, 4, 5]

def even():
    if x % 2:
        return "Even"
    else:
        return "False"

#Q7.]

try:
    num=int(input("Enter a number to divide 100 by:"))
    result=100/num
    print(f"Result:{result}")
except ValueError:
    print("Invalid input! Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divisible by zero")

# Q8.]
numbers = [1, 2, 3, 4, 5]

even_odd=["Even" if x%2 ==0 else "Odd" for x in numbers]
print(even_odd)

#Q9.]
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    result=a/b
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Infinite")

# Q10.]

num=int(input("Enter the number to evaluate table:"))
table=[num*i for i in range(1,11)]


with open("tables.txt","a") as f:
    f.write(f"Table of {num} :{str(table)} \n")

square=[x**2 for x in range(1,21) if x % 2==0]
print(square)



