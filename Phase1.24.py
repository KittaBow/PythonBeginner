#fahrenheit and celsius conversion formulas

#c=(f-32)*5/9
#f=(c*9/5)+32

temp = input("What's the temperature (degree) :") #45c

degree = int(temp[:-1]) #exempt the last one
unit = temp[-1].upper() #only the last one

print(degree," = ", unit)

#if "C":
    #converse to f
if unit=="C":
    result=(9*degree)/5+32
    unit_result="fahrenheit"

#if "F":
    #converse to c
if unit=="F":
    result=(degree-32)*5/9
    unit_result="celsius"

print("converse number = ",temp,"to", unit_result," = ",result)

