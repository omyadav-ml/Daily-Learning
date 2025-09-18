# # # for i in range (1,10):
# #     # print(i)
# # # While loop
# # i=1
# # while i<=50:
# #     print("om")
# #     i+=1


# # l1=['lion','tiger','elephant','bull','crazy']

# # i=0
# # while i<len(l1):

# #     if l1[i]=="elephant":
# #         break

# #     print("IT'S animal",l1[i])
# #     i+=1



# # # d1={
# #     1:"number",
# #     "om":"string",
# #     23.34:"Float",
# #     "true":"boolean"
# # }
# # print(d1.value())
# # for i in d1:
# #     print(i)
# erroe cause for loop is only iterates with list ,tuples and string.



for i in range (6,61,6):
    print(i)


# # To exit the loop now
# for i in range (25):
#     if(i==12):
#         break
#     print(i)

# # Used for skip values
# for i in range (25):
#     if(i==12):
#         continue
#     print(i)


# for i in range (25):
#     if(i==12):
#         pass
#     print(i)



# for i in range (5,51,5):
#     print(i)

# list= ["Harry", "Soham", "Sachin", "Rahul"] 

# # while i<len(list):
# #     print("Hello",list[i])
# #     i+=1

# for name in list:
#     if(name.startswith("S")):
#         print(f"Hello {name}")


# n=int(input("Enter a Number: "))
# i=1
# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i+=1 


# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"The factorial of : {n} is {fact}")


# n=int(input("Enter the number:"))
# for i in range(1, n+2):
#     if(i==1 or i==n):
#      print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")


for i in range(1,5):
    print("*" * i)
for i in range(5,0,-1):
    print("*"*i)

rows=9
for i in range(1,rows+1):
    spaces =rows-i
    stars=2*i-1
    print(" "* spaces+"*" *  stars)