# การค้นหาจำนวนตัวอักษรในสมาชิก

message=["aa", "aab", "cba", "bba", "abb", "cca"]
# หาว่าแต่ละช่องมี a กี่ตัว
result=[]

for item in message:
    result.append(item.count("a"))
print(result)

    
