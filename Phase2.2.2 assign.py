# การจับคู่สินค้าและราคา

fruit=["mango", "banana", "guava"]
price=[50,30,15]

for x,y in zip(fruit,price):
    print("product = ",x, "price = ",y)

for x,y in zip(fruit,price[::-1]):
    print("product = ",x, "price = ",y)