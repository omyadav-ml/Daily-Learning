def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error : cannot divide by zero "
    return a/b

while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.Exit")

    choice=input("Choose an option (1 to 5): ")

    if choice == "5":
        break


    if choice in ["1","2","3","4"]:
        try:
            num1=float(input("Enter a number: "))
            num2=float(input("Enter a number: "))
        except ValueError:
            print("Invalid input ! Enter number only")
            continue
        if choice == "1":
            result= add(num1,num2)
        elif choice == "2":
            result= sub(num1,num2)
        elif choice == "3":
            result= mul(num1,num2)
        elif choice == "4":
            result= div(num1,num2)

        print("Result",result)

    else:
        print("Invalid choose Selcet between 1 to 5")