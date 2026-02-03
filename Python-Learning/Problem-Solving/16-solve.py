a1=int(input("Enter 1st angle: "))
a2=int(input("Enter 2nd angle: "))
a3=int(input("Enter 3rd angle: "))
total=a1+a2+a3

if total== 180 and a1>0 and a2>0 and a3>0:
    print("It is a triangle")
else:
    print("It is not an triangle")

# print("It is Triangle" if total== 180 and a1>0 and a2>0 and a3>0 else "It is not an triangle" )