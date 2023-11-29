# เกมทายลูกเต๋า
# 1,2,3,4,5,6

import random
# สุ่มเลขลูกเต๋า
myrandom = random.randrange(1,7) # 1-6
k=1
correct=False
print("you have 3 chances to answer \n")
while True:
    number=int(input("fill answer = "))
    
    correct = number==myrandom # boolean: true/false

    if not correct :
        if(number>myrandom):
            print("less")
        if(number<myrandom):
            print("more")

    if correct :
        print("correct get 1 million")
        break
    if number<0 or k==3:
        break
    k+=1
if not correct :
    print("apologize, you lost")
    print("answer = ", myrandom)