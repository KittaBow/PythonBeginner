# Non primitive data type
# นำข้อมูล primitive มาประยุกต์ใช้ด้วย
# non-primitive ตัวแปร 1 ตัวเก็บค่าได้มากกว่า 1 ค่า มี 2 แบบคือที่สามารถเปลี่ยนแปลงชุดข้อมูลได้/เปลี่ยนไม่ได้

# List 
# ถ้าเก็บแบบ primitive
# a=1
# a1=2
# a2=3
# a3=4
# a4=5
# a5=6
# a6=7
# non-primitive: เป็นตัวเลขหรือข้อความก็ได้

number=[] # empty list
number=[1,2,3,4,5,6]
name=["A","B","C"]
all=[10,"A",True,3.14,-12]

#consructor
#name=list(["A", "B", "C"])
print(name)
print(all)

# เข้าถึงข้อมูลของ list
number[2]
print(number[2]) #ตัวเลขลำดับที่ 2 และใส่่ติดลบได้
print(name[1])
print(all[1:4]) #0,1,2,3

# การแก้ไขข้อมูล
# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"

print("ก่อนแก้ไข => ", number)

number[2]=9
number[5]=10
print("หลังแก้ไข => ",number)