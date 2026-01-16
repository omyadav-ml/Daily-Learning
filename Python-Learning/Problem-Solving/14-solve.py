a=int(input("Enter your age:"))
b=int(input("Enter your age:"))
c=int(input("Enter your age:"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)

oldest=max(a,b,c)
print(oldest)

# celcius=float(input("Enter celsius: "))
# fareheit=(celcius * 9/5)+32
# print("Farenheit- ",fareheit)


# a=int(input("a:"))
# b=int(input("b:"))

# a,b=b,a

# print(a,b)

# sum=lambda a,b,c:a+b+c
# print(sum(1,2,3))

num=(input("Enter digits : "))
print(sum(int(d) for d in num))

