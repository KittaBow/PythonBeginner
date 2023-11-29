# Find exponent

number=[1,2,3,4,5,6,7]

print(number)
# normal form
# for i in range(len(number)):
#     number[i]=number[i]*number[i] # หรือใช้ number[i]**2 ก็ได้
# print(number)

# ลดรูป
number=[i*i for i in number]
print(number)