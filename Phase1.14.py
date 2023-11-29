#control structure
#selected control sructure

#result is boolean การเปลี่ยน int เป็น boolean ใช้ ==

age=int(input("fill your age: "))
print(type(age==15))

#If boolean expression:
#   statement
#if must be true condition
if age>=15 and age<=20:
    print("teenager")
elif age>=20 and age<=29:
    print("working age")
elif age>=30 and age<=39:
    print("adult")
elif not age<=40:
    print("eldery")

#in case of being not true condition, use else
else :
    print("childhood")

#Ternary Operator
#"true condition" if expression else "other condition"
#print("teenager") if age>=15 and age<=20 else print("")


print("end")

#condition
# 15 - 20 => วัยรุ่น
# 21 - 29 => วัยผู้ใหญ่
# 30 - 39 => วัยทำงาน
