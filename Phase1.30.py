# Find Maximum / Minimum

max, min = 0,9999

while True : # infinity loop
    number=int(input("fill number :"))
    #กระโดดจาก loop
    if number<0 :
        break
    if number>max : 
        #ตอนแรกกำหนด max=0 จึงต้องกำหนดใหม่ว่าถ้า number ที่ถูก user ป้อน>0 เลขนั้นจะกลายเป็น max
        max=number
    if number<min:
        min=number
#จะเก็บตัวเลขไปเรื่อย ๆ จนกว่าจะกรอกเลขติดลบ มันจึงจะ print
print("maximum =",max)
print("minimum =",min)
