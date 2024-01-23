# Non-primitive: Set
# หลักการเหมือน set ทางคณิตศาสตร์
# {} ข้อมูลต่างชนิดกัน,แก้ไขสมาชิกไม่ได้,ซ้ำกันไม่ได้,ลำดับไม่แน่นอน,เพิ่มข้อมูลได้

# สร้างข้อมูลที่เป็น list constructor
fruit={"mango", "tamarind", "orange"}

# ที่บอกว่าไม่สามารถแก้ไขข้อมูลได้เพราะ ระบุ index ไม่ได้
# ใช้การสร้างแบบ constructor ช่วย
fish=set(["catfish", "cichlidfish"]) # ข้อมูลห้ามซ้ำกัน มันจะแสดงผลแค่ตัวเดียว

# ตย.การใช้ประโยชน์ คือ ถ้าเรามีข้อมูลที่ซ้ำกันเยอะๆ แล้วอยากให้กรองที่ซ้ำออก
# ก็เอาข้อมูลเข้า set

# การเพิ่มข้อมูลสมาชิก take exactly one argument
fruit.add("durian")
fruit.add("pineapple")

# ถ้าอยากเพิ่มทีละหลายๆตัว ก็สร้าง variable list ก่อน
lis=["apple","strawberry"]
fruit.update(lis)
# หรือไม่ต้องสร้างตัวแปรใหม่ โดยการ
fruit.update(["melon", "prum"])

# Use Loop for access data
for item in fruit:
    print("data =>", item) # ดึงสมาชิกแต่ละตัวออกมาแสดงผล 

# Count data members
print(len(fruit))

# check member
if "banana" in fruit:
    print("yes")
else:
    print("no")

# หรือลดรูปได้อีก เช่น
print("banana" in fruit) # outcome is true/false

# Delete members can use fn: remove, discard
fruit.remove("durian")
# if use remove fn, but dont have durian in data set, outcome is "error"
# if dont wanna show "error" have to use discard fn
fruit.discard("watermelon")
# clear.fruit() คือลบสมาชิก, del fruit คือลบตัวแปรเลย
print(fruit)

