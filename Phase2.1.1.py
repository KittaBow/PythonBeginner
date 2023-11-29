#number=[1,2,3,4,5,6] # list มีสมาชิก 1-6
# การแก้ไขข้อมูล
# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
#sum=0
#for x in number:
#    sum+=x # sum=sum+x
#print(sum)

#for item in number:
#    print(item)

number=[1,2,3,4,5,6,7,8,9,10] #list มีสมาชิก 1-6
fruit=["mango", "lemon", "mayom"]

if 20 in number:
    print("have")
else:
    print("no have")

# counting members, size of list
print(len(number))
print(len(fruit))

for i in range(len(fruit)):
    print(fruit[i])

#adding information, take exactly one!!!
print("before adding=>", fruit)

fruit.append("banana")
fruit.append("watermelon")
#insert (index,member) จะให้ไปแทรกที่ตำแหน่งไหน
print("after adding=>", fruit)
fruit.insert(1,"durian")
print("insert=>", fruit)
