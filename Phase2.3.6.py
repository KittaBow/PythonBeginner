# Non-Primitive
# Dictionary
# ลักษณะคล้ายกับ set, fusion between tuple and set

lis=["red", "yellow", "green"]
tup=["red", "yellow", "green"]

print(lis)
print(tup)

# run by index จะเข้าถึงข้อมูลง่ายถ้ารู้ index ไหนคือ value อะไร
print(lis[0])
print(tup[0])
# แต่ถ้าไม่รู้ index and value ต้องใช้ dictionary ช่วย

# dictionary => key (การเข้าถึงข้อมูล,เป็น string ได้ทุกแบบ), value (ค่าของข้อมูล)
# list, tuple => index (ต้องระบุเป็น integer เท่านั้น), value

# การสร้าง dictionary มี 2 แบบ
# variable name = {key:value, key:value, key:value}
# สามารถเรียกข้อมูลจาก key ได้เลย ไม่ต้องจำ index
colors={"red":"สีแดง", "yellow":"สีเหลือง", "green":"สีเขียว"}
print(colors["red"])

# create by constructor
pets=dict(cat="แมว", dog="หมา", duck="เป็ด")
# access data in 2 ways
print(pets["duck"])
print(pets.get("cat"))
# adding data to dictionary use update fn
pets.update({"bird":"นก"})
print(pets)

# Loop 
# show only key
for item in pets:
    print(item)

# if wanna show only value use
for item in pets.values():
    print(item)

# if wanna show both use
for item in pets.items():
    print(item)

# show outputs in advance
for k,v in pets.items():
    print("key =",k,"value =",v)

# Deletion use pop fn
pets.pop("cat")
print(pets)
# pets.popitem() ลบข้อมูลที่อยู่ท้ายสุดออกไป

# การเคลียร์สมาชิกทั้งหมด > pets.clear()
# การลบตัวแปร > del pets

# Copy dictionary
x=pets.copy()
print(x)

# Dictionary ซ้อนกัน
# ex1
market1={
    "Pron":"food shop",
    "Pom":"fruit shop",
    "Jai":"drink shop"
}
print(market1)

# ex2 ข้อมูลใน dict สามารถระบุได้หลายประเภท string ทั้งหมดเลย
market2={
    "store A":{
        "owner":"Pron",
        "menu":"noodles",
        "area":"Bangna"
    },
    "store B":{
        "owner":"Pom",
        "menu":"fruits",
        "area":"Thonglor"
    },
    "store D":{
        "owner":"Jai",
        "menu":"drinks",
        "area":"Silom"
    },

}
print(market2)
# หาข้อมูลแบบเจาะจง
print(market2["store A"]["menu"])
# หาข้อมูลแบบเจาะจง 
print("fruit" in market2["store B"]["menu"]) #ถ้าไม่ระบุว่า menu จะหาไม่เจอ

if "drinks" in market2["store D"]["menu"]:
    print("have")
else :
    print("no have")

