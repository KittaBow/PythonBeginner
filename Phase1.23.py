#deep string using

name = " kittayaporn: 26 " # index => 0 นับรวมช่องว่าง

print(name[0:3]) #show data before 3 (0,1,2)
#use bracket to specify the data to be displayed

print(name[-1]) #the last one
print(name[-2:]) #before the last one onwards

#count the number of characters
print(len(name))

#delete space 
name=name.strip() #can define left or right to delete(lstrip/rstrip)
print(len(name))

#change lower to upper front
print(name.upper())
#change only the first to upper
print(name.capitalize())

#replacement
print(name.replace("kitta","kitti"))
detail= "kitta grade 4 room 3"
print(detail.replace("4","5",1)) #change number 4 to 5 only position1

#fine some word in data, boolean
x = "ya" in name
print(x)
if x:
    name=name.replace("ya","yaa")
print(name)