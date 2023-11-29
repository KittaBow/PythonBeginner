# ตัวเลขขั้นบันได

last=int(input("fill number :"))

for row in range(1,last+1):
    for column in range(1,row+1): 
        print(column, end='')
    print(" ")

# input = 3
# row = 1 , 3
# column 1,2(1+1)
# 1
# row 2
# column 1, 3
# 12

# row 3
# column 1,4
# 123