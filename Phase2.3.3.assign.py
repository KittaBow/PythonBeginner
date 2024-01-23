# Tuple tutorial
# นำค่าใน tuple ไปใส่ในตัวแปร
tup=(10,20,30)
a,b,c=tup # create tuple variable 
#  เป็นการจับคู่ 10,a 20,b 30,c
print(a)
print(b)
print(c)

d=a+c
print(d)

# สลับ tuple 
x=(50,60)
y=(88,99)
print("before x =>",x)
print("before y =>",y)

x,y=y,x
print("after x =>",x)
print("after y =>",y)

# change tuple to string
character=('k','o','n','g')
# แปลงตัวอักษรใน character => string
name="".join(character)
# แต่ join เป็น string จึงต้องเขียนร่วมกับสัญลักษณ์ double code ("".)
print(name)

# reverse tuple สมาชิกท้ายสุดมาอยู่หน้าสุด
z=(100,20,30,15,10,5,500)
r=reversed(z)
# print(r) เลยไม่ได้ เพราะมันเป็น object ต้องแปลงเป็น tuple or list ก่อน
print(tuple(r)) # หรือใช้ syntax r=tuple(reversed(z))

# reverse string to tuple
s="kittayaporn"
t=tuple(s)
print(t)


