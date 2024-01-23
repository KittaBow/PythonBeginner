# Tuple ปกติข้อมูลตรงนี้จะแก้ไม่ได้
tup=(1,2,3,4,"Kong","mango", True, 3.3)
# 0 - >
# print(tup[:-1])
# tup[0]="bangkok"
# ถ้าอยากแก้ไขสมาชิกใน tuple ก็แค่แปลงให้มันเป็นกลุ่ม list
print("before edit =>", tup)

lis=list(tup)
lis[0]="bangkok"
# แก้ไขเสร็จแล้วก็แปลงกลับเป็น tuple
tup=tuple(lis)
print("after edit =>", tup)




