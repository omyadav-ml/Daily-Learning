# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

def descending_order(num):
    return int("".join(sorted(str(num),reverse=True)))

    # "".join used for join the number without separation
    # sorted use for sort the num
    # str(num) convert the num into string so 456 is "456"
    # # reverse=True is main it reverse the num means is num is 123 using reverse=true it will be 321

print(descending_order("981234756"))
