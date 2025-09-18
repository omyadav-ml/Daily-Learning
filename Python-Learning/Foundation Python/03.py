# random = ["desk", "chair", "table", "lamp", "sofa", "bed", "shelf", "cabinet"]
# print(random[1:5])  

l1=[3,4,2,6,9]

l1.sort()
print(l1)
                
l1.reverse()
print(l1) 

l1.append(100)
print(l1)

l1.insert(2,5)
print(l1)

l1.remove(5)
print(l1)

l1.pop(3)
print(l1)

l1.clear()
print(l1)

tuple1 = (1, 2, 3, 4, 5)
print(tuple1[1:4])  # Slicing a tuple

# location = (28.6139, 77.2090) #(latitude, longitude)
# print(location)  # Parinting a tuple representing a location

# dict and sets
things={
    "pen":"pencil",
    "notebook": "eraser"
    } 
print(things["notebook"])
print(things.get("pen"))  # Using get method to access dictionary value
print(things.items())  # Printing all items in the dictionary in tuples like (pen,pencil)
print(things.keys())  # Printing all keys in the dictionary
print(things.values())  # Printing all values in the dictionary
things.update({"notebook": "sharpener"})  #
print(things) 
#  # Updating 


# colors = {
#     "apple": "red",
#     "banana": "yellow",
#     "grapes": "purple",
# }
# print(colors["banana"])  


student = {
    "name": "Om",
    "age": 19,
    "course": "BSc IT",
  
}
student.update({"age":20,"marks":88})  
print(student,type(student)) 
print(student.get("course"))  

