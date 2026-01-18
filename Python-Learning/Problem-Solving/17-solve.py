cost_price=int(input("Enter cost price: "))
selling_price=int(input("Enter sellinng price: "))

if cost_price<selling_price:
    print("Its Profit ")
elif cost_price==selling_price:
    print("Nor profit Nor loss")
else:
    print("Its loss")
