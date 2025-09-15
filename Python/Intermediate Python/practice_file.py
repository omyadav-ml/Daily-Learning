# Q1.]

# a=open("file.txt")
# content=a.read()
# if("world" in content):
#     print("it contains the word")
# else:
#     print("no it dose'nt contain the word")
# a.close()

# # Q2.]

# with open("file.txt","r") as f:
#     word=f.read()
# new_word=word.replace("Twinkle","#####")
# with open("file.txt","w") as f:
#     word=f.write(new_word)

# Q3.]
# word=(little star)
# with open("file.txt") as f:
#     word=f.read()

# censord=word.replace("liitle star","########")
# print(censord)

# Q4.]

# with open("text.txt") as f:
#     c=f.read()

# if("python" in c):
#     print("Yes python is present")
# else:
#     print("NO there is no python ")

# Q5.]

# with open("file.txt") as f:
#     a=f.read()

# with open("this_copy.txt","w") as f:
#     f.write(a)

# Q6.]

# with open("file.txt") as f:
#     content_1=f.read()

# with open("this_copy.txt") as f:
#     content_2=f.read()

# if(content_1 == content_2):
#     print("Yes this file content is similar")
# else:
#     ("No the content is not similar")

# # Q7.]

# with open("this_copy.txt", "r+") as file:
# #     file.truncate(0)

# with open("this_copy.txt", "w") as file:
#     file.write("")  # Changed 'f' to 'file'

with open("myfile.txt") as f:
    content=f.read()

with open("Renamed_python.txt","w") as f:
    f.write(content)