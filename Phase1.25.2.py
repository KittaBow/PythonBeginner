#while loop assignment


i=1 #round counter
# 1+2+3+4+5
summation = 0 #เก็บผลการบวกเลขตามจำนวนรอบ
average = 0 # ผลรวม/จำนวนรอบ

#เลข 1 เป็นตัวเริ่มต้น ให้ทำงาน 10 ครั้ง
while i<=10:
    summation+=i # เก็บผลรวมของ i แต่ละรอบ 1 + 2
    print("round =", i,"sum =" ,summation)
    i+=1 # 1,2,3,4,5

    #ลูปเอาค่า i ไปเก็บที่ sum แล้ววนมาบวกที่ i อีก แต่ต้องเช็คเงื่อนไข while ทุกครั้งด้วย

average=summation/10

print("sum =", summation)
print("average =", average)

