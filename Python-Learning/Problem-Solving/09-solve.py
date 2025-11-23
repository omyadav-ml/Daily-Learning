lst = ['level','hello','madam','world','noon']
palindrome=[n for n in lst if str(n)==str(n)[::-1]]
print(palindrome)