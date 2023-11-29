# Delete from list

number=[1,2,3,4,5,6,7,8,9,10,5,6,5,3]
fruit=["mango", "lemon", "durian", "mayom", "banana", "watermelon"]
fruits= ["mango", "lemon", "durian", "mayom", "banana",]
# Remove, specific deletion
fruit.remove("mayom")
print("remove =>",fruit)

# Pop, delete the last one
fruit.pop()
print("pop =>", fruit)

# Del, del variable[index]
del fruit[1]
print(fruit)

# Clear, clear only members of list
fruit.clear()
print(fruit) 

# Copy from list
x=[]
print(x)
x=number.copy()
print(x)

# Merg list
allGroup=number+fruits
print(allGroup)

# Counting members
y=number.count(5)
print(y)

# Extend เอาสมาชิกของ list นึง ไปใส่อีก list นึง ไม่ต้องสร้าง list ก้อนใหม่
number.extend(fruits)
print(number)