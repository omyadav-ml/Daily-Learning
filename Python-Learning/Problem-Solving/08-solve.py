lst = [1,3,5,15,16]
replace=['Fizz' if x%3==0 else 'Buzz' if x%5==0 else x for x in lst]
print(replace)

# Q2.]

a=[1,2,3]
b=[4,5,6]

products=[x*y for x in a for y in b if x*y > 10]
print(products)