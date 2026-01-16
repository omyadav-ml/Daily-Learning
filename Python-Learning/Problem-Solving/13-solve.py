# try:
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     result=a/b

# except ZeroDivisionError:
#     print("The number cannot divided by zero")

# except ValueError:
#     print("Enter valid integer")

# else:
#     print("Result:",result)

# finally:
#     print("Program Ended")



# try:
#     a=(input("Enter a string:"))
#     b=int(a)

# except ValueError:
#     print("Enter a valid input")

# else:
#     print(b)

# numbers=[1,2,3,4,5]

# try:
#     index=int(input("Enter the index: "))
#     print(numbers[index])
 
# except IndexError:
#     print('Index out of range')

# except ValueError:
#     print("Please enter a valid integer index")


while True:
    try:
        a=int(input("Enter number: "))
        b=int(input("Enter number: "))
        result=a/b

    except ValueError:
        print("Enter a valid integer")

    except ZeroDivisionError:
        print("The number cannot divided by zero!")

    else:
        print("Result",result)
        break
    finally:
        print("Program excution completed")


while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.Exit")

    choice=input("Enter your choice")

    if choice == "5":
        break

try:
     a=int(input("Enter number: "))
     b=int(input("Enter number: "))

     if choice == "1":
         print(a+b)

     elif choice =="2":
         print(a-b)

     elif choice == "3":
         print(a*b)
         
     elif choice == "4":
         print(a/b)

     else:
         print("Invalid Input")

except ValueError:
    print("Enter a valid integer")    

except ZeroDivisionError:
    print("Cannot Divide by Zero")




