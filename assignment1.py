#BMI calculate program
#BMI = weight (kg)/ height * height (m)

 #input / convert to integer
weight=int(input("fill your weight (kg): "))
height=int(input("fill your height (cm): "))

#process
#cm => m
height=height/100

#calculate BMI
bmi=weight/(height*height)

#output
print("BMI = " ,bmi)

