# sourcing data
tup=(100,99,88,50,200,1,2,3,4,3,99,4) #tuple
print("before =>", tup)
# tup.sort() ไม่มี ต้องแปลงเป็น list ก่อน
lis=list(tup)
lis.sort() # แปลงกลับด้วย
# lis.reverse() เรียงย้อนกลับจากมากไปน้อย
tup=tuple(lis)

print("after =>", tup)

