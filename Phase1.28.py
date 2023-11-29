#break / continue
#break = stop loop, continue = jump step

i=1
while i<=10:
    print("round =",i)
    if(i==5):
        break #ที่จริงต้องลูป 10 รอบแต่เราสั่งเบรคที่ 5
    i+=1
else:
    print("end")
print("end")

i=0 
while i<=10:
    i+=1
    if(i==5):
        continue
    print("round =",i)
print("end")

i=0
while i<10:
    i+=1
    if(i%2 == 0):
        continue
    print("round =",i)
print("end")

for i in range(1,11):
    if(i%2 == 0): #กระโดดข้ามค่าที่หาร 2 ลงตัว
        continue #ถ้าใส่ break คือไม่แสดงผลเงื่อนไขหลัง if
    print(i)
print("end")


