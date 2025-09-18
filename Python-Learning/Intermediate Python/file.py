#  # To read File
# a=open("file.txt")
# data=a.read()
# print(data)

# a.close()

# # To write File
# a="Om What you Doing Rn,Chilling :"
# f=open("myfile.txt","w")
# f.write(a)
# f.close()

# # To append file
# a="Nah Man Just Grinding"
# f=open("myfile.txt","a")
# f.write(a)
# f.close()

# # To readline the file
# f=open ("file.txt")
# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line3=f.readline()
# print(line3,type(line3))

# line4=f.readline()
# print(line4,type(line4))

# line5=f.readline()
# print(line5,type(line5))

# line6=f.readline()
# print(line6 =="")
# f.close()

# To use while loop for read line the file
# f=open ("file.txt")
# line=f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
# f.close



# To use [with] statement to ignore close statement
#  Open the file in read mode using 'with', which automatically closes the file 

# Before
# a=open("file.txt")
# print(a.read())
# a.close()

# After
# with open("file.txt") as a:
#     print(a.read())

