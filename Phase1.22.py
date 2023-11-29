#Upgrade BMI program

#BMI = weight (kg)/height**2 (m)
#input / convert to integer

weight=int(input("fill your weight (kg): "))
height=int(input("fill your height (cm): "))/100

bmi = weight/(height**2)
#use If else to divide the range of BMI

if bmi>=0 and bmi<=18.0:
    result = "underweight"
elif bmi>=18.5 and bmi<=24.9:
    result = "healthy"
elif bmi>=25.0 and bmi<=29.9:
    result = "overweight"
elif bmi>30:
    result = "obesity"
else:
    result= "can't divide"

print("BMI= ", bmi, "range= ", result)


#Adult Body Mass Index
#<18 = underweight
#18.5 - 24.9 = healthy 
#25.0 - 29.9 = overweight 
#>30 = obesity 


