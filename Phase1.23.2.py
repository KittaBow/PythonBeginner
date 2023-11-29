#deep string using 
#

fname = "kittayaporn"
lname = "nualsuwan"
age = "26"
salary = 28000.058484

fullname = fname+lname+age
#print("Name :"+fname+"\tLast name :"+lname)
#format form
#text= "Name :{}\tLast name :{}\tAge :{}"

#print(text.format(fname,lname,age))

#can make sequeance of data
text= "Name :{0}\tLast name :{1}\tAge :{2}\tSalary :{3:.2f}"
print(text.format(fname,lname,age,salary))

#how many words?, count fn
fruit= "go to buy durian mangosteen durian-strickyrice at the market and go to durian garden"
print(fruit.count("durian"))

#check the first word of the sentence
print(fruit.startswith("to"))

if fruit.startswith("go"):
    print("yes")
else :
    print("no")

if fruit.endswith("garden"):
    print("yes")
else :
    print("no")
