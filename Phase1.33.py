# ตารางหมากฮอต

# x = brown
# o = white
# แถวแรกเลขคี่สีขาว, เลขคู่สีน้ำตาล แถวถัดไปสลับกัน

number=int(input("fill size ="))
for row in range(number):
    for column in range(number):
        if column in range(number): # กำหนดแถวสลับ
            if (row+column)%2 == 0:
                print("x", end = "")
            else :
                print("o", end = "")
    print(" ")

# 3 x 3
# row = 0 + column = 0
# row = 0 + 1 > else
# row = 0 + 2

# row = 1 + column = 0
# row = 1 + 1 
# row = 1 + 2 > else

# row = 2 + column = 0
# row = 2 + 1 > else
# row = 2 + 2

#result 
# xox
# oxo
# xox