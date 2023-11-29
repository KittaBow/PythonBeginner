#Pass use when you don't wanna set some conditions, to run through
age=int(input("fill your age: "))

if age<=15:
    if age==15:
        pass
    elif age==14:
        pass
    else :
        print("primary school")
else :
    print("high school")

print("end")