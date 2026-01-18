# function defination
def fun():
    print("Have A Great Day")
    # fun()
# function call
fun()
print("Thank You")
# fun()
# def factorial(n):

# #     if n == 0 or n==1:  
# #         return 1 
# #     else: 
# #         return n*factorial(n-1)

# # n=int(input("Enter a Number:"))

# # print(f"The factorial of this number is : {factorial(n)}")

# a=23
# b=34
# c=12
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a

#     elif(b>a and b>c):
#         return b

#     elif(c>b and c>a):
#         return c
# print(greatest(a,b,c))
# greatest(a,b,c)

# def f_to_c(f):
#     return 5*(f-32)/9

# f=int(input("Enter temperature in F:"))
# # print(f"{f_to_c}Degree C")

# print("a")
# print("b", end="")
# print("c", end="")

num=int(input("Enter a Number to sum: "))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
a=(sum(num))
print(f"Sum of numbers from 1 to {num} is: {a}")


