def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Error : cannot divide by zero "
    return a/b
def power(a,b):
    return a**b

while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.Pow")
    print("6.Exit")

    choice=input("Choose an option (1 to 6): ")

    if choice == "6":
        break


    if choice in ["1","2","3","4","5"]:
        try:
            num1=float(input("Enter a number: "))
            num2=float(input("Enter a number: "))
        except ValueError:
            print("Invalid input ! Enter number only")
            continue
        if choice == "1":
            result= addition(num1,num2)
        elif choice == "2":
            result= subtraction(num1,num2)
        elif choice == "3":
            result= multiply(num1,num2)
        elif choice == "4":
            result= division(num1,num2)
        elif choice == "5":
            result= power(num1,num2)

        print("Result",result)

    else:
        print("Invalid choose Selcet between 1 to 5")