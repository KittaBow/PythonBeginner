# Loop for tuple
tup=(1,2,3,4,"Kong","mango",True,3.3)

for item in tup:
    print("member = ",item)

# check member
if "durian" in tup:
    print("is member")
else:
    print("isn't member")

if True in tup:
    print("is member")
else:
    print("isn't member")

# count member
print(len(tup))

for item in range(len(tup)): #range 0-8
    print(tup[item]) # tup[0], tup[1],...tup[7]

# การสร้าง tuple แบบไม่มีสมาชิก
# x=() ก็ได้
# หรือสร้างแบบ constructor
x=tuple() # empty tuple
print(x)
x=("Kong", ) # 1 member  ถ้าไม่ใส่ , มันจะมองว่าเป็น string

name=("Kong", "Bo")
# ถ้าต้องการเพิ่มสมาชิก nut ต้องทำข้อมูลเป็น tuple ถ้า new=("Nut") รูปแบบนี้โปรแกรมจะมองเป็น string
new=("Nut", )
# ถ้าเป็น tuple แล้ว + ข้อมูลต่อกันได้เลย
name=name+new
print(name)
# การเพิ่มสมาชิก tuple ทำได้หลายแบบแต่ต้องเลือกให้เหมาะ
# จะเพิ่มสมาชิกเข้าไปในตัวแปรเดิมหรือ รวมกันแล้วสร้างตัวแปรใหม่ก็ได้
# ตย.การเปลี่ยน list to tuple ง่ายๆ
city=["BKK", "Chonburi", "Ubon"]

tuple(city)
tup=tup+tuple(city)
print(tup)