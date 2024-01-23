# Set Operator
# ถ้ามีหลายเซ็ท และอยากให้มันดำเนินการร่วมกัน
# ใช้หลัก Union Intersect

fruitA={"banana", "gooseberry", "lemon", "durian"}
fruitB={"strawberry", "kiwi", "mango", "durian"}

# allfruit=fruitA.union(fruitB)
# print(allfruit)
# operate โดยไม่ต้องสร้างตัวแปรใหม่โดย
# fruitA.update(fruitB)
print(fruitA)

# copy fn
fruitC=fruitA.copy()
print(fruitC)

# difference แยกสมาชิกแต่ละเซ็ทว่าแตกต่างกันอย่างไร
fruitD=fruitA.difference(fruitB)
print("D =>",fruitD)
# ลดรูปโดยไม่ต้องสร้างตัวแปร D 

# fruitA.difference_update(fruitB)
# print(fruitA)

# intersect แสดงผลสมาชิกที่เหมือนกัน
fruitF=fruitA.intersection(fruitB)
print("F =>",fruitF)
# ลดรูปโดยไม่ต้องสร้างตัวแปร F

# fruitA.intersection_update(fruitB)
# print(fruitA)

# Subset เปรียบเทียบว่า set ที่สร้าง เป็น subset ของ set หลักมั้ย
fish={"catfish", "cichlidfish", "whale", "shark"} # called superset

# x={"cichlidfish", "minnow"} ถ้าตัวแปรใดตัวแปรนึงไม่อยู่ใน subset=False
x={"cichlidfish", "whale"} # called subset
print(x.issubset(fish))

# Set operator
# min,max

number={3,4,5,100,80,900,1000,500,300,-100,-8,-150}

print(sorted(number))
print(min(number))
print(max(number))

# frozen set ไม่สามารถแก้ไข หรือทำอะไรกับมันได้เลย cant add or delete
fruit=frozenset(["mango", "gooseberry", "lemon"])
for item in fruit:
    print("data =>", item) 



