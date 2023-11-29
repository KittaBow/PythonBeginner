# Assignment รับและเรียงข้อมูลตัวเลข
number=[]
odd=[] # odd number
even=[] # even number

while True:
    x=int(input("fill number: "))
    if x<0:
        break
    if x%2 == 0:# หากลุ่มเลขคู่หรือเลขคี่
        even.append(x)
    else :
        odd.append(x)
    number.append(x) #ตัวเลขที่ผู้ใช้ป้อน จะต่อกันเรื่อยๆ โปรแกรมจะจบตอนที่กรอกเลขน้อยกว่า 0
 
print("before sort =>", number)
number.sort()
print("after sort from less =>", number)
number.reverse() 
print("reverse from higher >", number)
print("maximum is", max(number))
print("minimum is", min(number))
print("summation is", sum(number))
print("odd number= ", odd)
print("even number= ", even)





