# to find a factorial by user
n=int(input("Enter a number for factorial: "))

def factorial(n):
    if n==0 or n==1:  #Base class
        return 1
    else:             #Recursive class
        return n* factorial(n-1)
    
print(f"The factorial of your number is:", factorial(n))
