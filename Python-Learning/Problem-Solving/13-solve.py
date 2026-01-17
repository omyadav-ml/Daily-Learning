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
