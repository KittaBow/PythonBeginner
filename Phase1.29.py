start, stop = 1,3
sum, avg=0,0 #เก็บผลรวมของตัวเลขที่เพิ่มเข้ามา
while(start<=stop):
    number=int(input("fill number: "))
    sum+=number #บวกเลขที่ป้อนแต่ละรอบ
    start+=1 

avg=sum/stop
print("sum =", sum)
print("avg =", avg)

sum = 0
while sum!=100: #ถ้าไม่เท่ากับ 100 ก็รันไปเรื่อยๆ มากกว่า 100 ก็ได้
    number=int(input("fill number: "))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    print("summation = ", sum)
print("end")

sum = 0
while True:
    number=int(input("fill number :"))
    sum+=number
    if sum>=100:
        break
    print("summation =", sum)
    
