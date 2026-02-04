from functools import reduce
square=lambda x:x*x
print(square(4))

sum=lambda a,b,c:a+b+c
print(sum(1,2,3))

# join function

a=["Om","Aryan"]
final = ":".join(a)
print(final)

a=["Om","Aryan"]
final = "-".join(a)
print(final)

#map method
# map(function, iterable)
# iterable means (list,tuple,dict,etc.)

numbers=[2,4,6,8]

def square(q):
    return q*q
result=map(square,numbers)
print(list(result))

# lambda with map

num=[1,3,5,7,9]
result=map(lambda x:x**2,num)
print(tuple(result))

# filter example
li=[1,2,3,4,5,6,7,8,9,10]

def even(x):
    if (x%2==0):
        return True
    return False
onlyEven=filter(even,li)
print(list(onlyEven))

# Reduce Function
def sum(a,b):
    return a+b
print(reduce(sum,li))

def subtract(a,b):
    return a-b
print(reduce(subtract,li))

mul=lambda x,y:x*y
print(reduce(mul,li))