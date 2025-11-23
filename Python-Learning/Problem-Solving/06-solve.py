# Check if a number is palindrome

def is_palindrome_num(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_num("Om"))