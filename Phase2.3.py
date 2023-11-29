# Tuple คล้ายกับ List ต่างกันที่ List สมาชิกเปลี่ยนแปลงได้แต่ Tuple เปลี่ยนไม่ได้
tup=tuple((1,2,3,4,"mango", "Kong", True, 3.9))
lis=list([1,2,3,4,"mango", "Kong", True, 3.9])

# เปลี่ยนตัวแรกของ lis เป็นคำอื่น
lis[0]="bangkok" # tuple ทำไม่ได้

print(tup)
print(lis)

# การเข้าถึงข้อมูล
print(tup[0:3])
print(tup[0:])
print(tup[-2])
print(tup[-3:-1])
# เวลาระบุขอบเขตของ index ต้องใช้ []


