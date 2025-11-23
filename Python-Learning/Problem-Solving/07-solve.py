# Q1.]
lst=[1,2,3,4,5,6,7,8,9,10]
even_squares=[x**2 for x in lst if x%2==0]
print(even_squares)

# Q2.]
lst=[1,2,3,4,5,6,7,8,9,10]
new_lst=[x**2 if x%2==0 else x**3 for x in lst]
print(new_lst)

#Q3.]
words=["C","C++","Python","Java","Html"]
long_words=[word for word in words if len(word)>3]
print(words)
