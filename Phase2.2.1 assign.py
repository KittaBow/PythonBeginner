# จับคู่คำทักทาย/ บุคคล

# Hi, Hello
# Kong, Kam
# Hi Kong, Hi Kam, Hello Kong, Hello Kam

greeting=["สวัสดี", "Hi", "Hello", "Good bye"]
people=["Kong", "Kam", "Jo"]
result=[]

# normal
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)

# ลดรูป
result=[x+y for x in greeting for y in people]
print(result)