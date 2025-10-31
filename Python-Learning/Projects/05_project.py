import statistics 

data=input("Enter numbers separted by commas:")
numbers=[int(num) for  num in data.split(",")]

mean=statistics.mean(numbers)
median=statistics.median(numbers)
mode=statistics.mode(numbers)

print("\nNumbers:",numbers)
print("\nMean:",mean)
print("\nMedian:",median)
print("\nMode:",mode)