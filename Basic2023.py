#For loop
for number in range(10):
    print(number)
for number2 in range(1,11):
    print(number2)

#While loop คือการทำซ้ำตามเงื่อนไขที่มีค่าเป็นจริง (True) แล้วเมื่อไหร่ที่เงื่อนไขเป็นจริง
#จะทำงานในลูปแบบไม่รู้จบ
while True:
    print('this is WHILE')
    break

name = 'Mr.A'
while name == 'Mr.A':
    print('Hello', name)
    break

#Enumerating Iterators การลำดับค่า จะมีฟังก์ชัน enumerate()ในการเพิ่มค่าการลำดับมาช่วย
#โดยสามารถกำหนดค่าเริ่มต้นได้เป็นพารามิเตอร์ตัวที่ 2 หลังจากตัวแปร names
names = ['Blue', 'Red', 'Pink']
for number, name in enumerate(names):
    print(f'{number}: {name}')

"""

Multi line comments

"""

'''



'''