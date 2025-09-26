import random
n=random.randint(1,100)
a=-1
guess=1
while(a!=n):
    a=int(input("Guess a number:"))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher Number please")
        guess+=1
print(f"You have guesssed the number {n} correctly in {guess} attempts")