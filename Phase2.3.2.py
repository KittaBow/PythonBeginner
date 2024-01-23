# how to delete 
tup=(1,2,3,4, "kong", "mango",True,3.9,4)
print("before =>", tup)
# change tuple to list
lis=list(tup)
lis.remove("mango")
# ลบมะม่วงเสร็จแล้วก็แปลงกลับเป็น tuple
tup=tuple(lis)

print("after =>", tup)

# count member นับว่ามีเลข 4 กี่ที่
x=tup.count(4)
print(x)
# fn index() หาว่าอยู่ index อะไร
y=tup.index(4)
print(y)
