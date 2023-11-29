#loop in loop

i=1 #ค่าเริ่มต้น

while i<=3:
    j=1 #ตัวนับจะไปทำซ้ำ loop while ดึง j ขึ้นมาเช็คเงื่อนไข <=3 หรือไม่ แล้วจึง print แล้วบวกบรรทัด 9
    while j<=5:
        print("round =",i,"position =", j)
        j+=1
    i+=1
#เช็คเงื่อนไข loop ข้างนอก ถ้าเป็นจริงก็เข้าไปวน loop ข้างในวนไป จนเจอตัวที่เงื่อนไขเป็นเท็จ

for i in range(1,4):
    print("round =",i)
    for j in range(1,6):
        print("position =",j)
#ทำ loop นอกก่อนแล้วเข้า loop ใน
