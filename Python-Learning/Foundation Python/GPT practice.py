# # name=str(input("Enter your name: "))
# # age=int(input("Enter your age: "))
# # print(f"Hello {name}, you are {age} years old.")


# # numbers = []

# # num = int(input("Enter number: "))
# # numbers.append(num)

# # num = int(input("Enter number: "))
# # numbers.append(num)

# # num = int(input("Enter number: "))
# # numbers.append(num)

# # num = int(input("Enter number: "))
# # numbers.append(num)

# # num = int(input("Enter number: "))
# # numbers.append(num)

# # print("Numbers in the list:", numbers)


# # print(sum(numbers))
# # print(max(numbers))
# # print(min(numbers))

tuple=("red", "green","blue", "yellow"," purple"," silver","blue")
print(tuple[1])  
print(tuple[4])
print(tuple.count("blue"))


# items=[23,34,45,56]
# print(items.reverse())
      
# fruits = ("apple", "banana", "mango", "orange")
# print(fruits)

name=input("Enter your name: ")
print(f"Hello {name}")
print("name",type(name))

cities = ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"]
intersection = set(cities)
print("Unique cities:", intersection)

s=set()
s.add(18)
s.add('18')
print(s)

s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))

from functools import reduce

nums=[2,3,4,5]
print(reduce(lambda a,b:a+b,nums))

