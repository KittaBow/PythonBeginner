#Loop, for ระบุจำนวนรอบการวนได้ชัดเจนกว่า while 
#while > ตัวนับ > เงื่อนไข > step
#for i in range สำหรับกำหนดรอบว่าจะให้ทำกี่รอบ (start, stop, step)>เป็นค่าติดลบได้

for i in range(3): #เริ่มที่ 0 ถ้าเป็นกำหนด i อื่นๆ จะเริ่มที่ 1
    print("round =", i,"Hello World")
print("end")

for i in range(2,6):
    print("round =", i, "Hi")
print("end")

for i in range(1,6,2): #เลข 2 เป็น step การเพิ่มจำนวนรอบ
    print("round =", i, "good bye")
print("end")

summation=0


for i in range(5):
    summation+=i
    print("round =", i, "sum =", summation)

print("sum =", summation)

for i in range(1,6):
    summation+=i
    print("round =", i, "sum =", summation)

print("sum =", summation)

for i in range(10,0,-1):
    summation+=i
    print("round =", i, "sum =", summation)
