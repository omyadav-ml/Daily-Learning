# # sets in non repitative data
items = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
items.add(0)
print(items)
items.update([11,12]) #for multiple items
print(items)
items.remove(0)
print(items)
items.discard(1)
print(items)
items.pop()
print(items)
items.clear()
print(items,type(items))

# Example program
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)   # Union → {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # Intersection → {3, 4}
print(set1 - set2)   # Difference → {1, 2}
print(set1 ^ set2)   # Symmetric Difference → {1, 2, 5, 6}


# translate ={
#     "hello":"नमस्ते" ,
#  "Thank you" :"धन्यवाद",
#  "good":"अच्छा"
# }
# means=input("Enter a word in Hindi: ")
# print(translate[means])
s=set()
n=input("Enter number: ")
s.update(n)
print(s)

# s = {8, 7, 12, "Harry", [1,2]}

dict={}
name=input("Enter friend's name: ")
language=input("Enter friend's language: ")
dict.update({name: language})

name=input("Enter friend's name: ")
language=input("Enter friend's language: ")
dict.update({name: language})

name=input("Enter friend's name: ")
language=input("Enter friend's language: ")
dict.update({name: language})

name=input("Enter friend's name: ")
language=input("Enter friend's language: ")
dict.update({name: language})

print(dict)


