#multiplication table

#2,3

for x in range(2,4):
    print("MT2 =",x)
    for y in range(1,13):
        print(x, 'x', y,"=", (x*y))
        #x=MT , 'x'=multi sign, y=multi posi

start=int(input("fill first multi table =")) #1
stop=int(input("fill last maulti table =")) #4

for x in range(start,stop+1): #จะรันถึงลำดับก่อนหน้า stop ถ้าอยากให้รันตรงลำดับเลขต้องใส่ +1 หลัง stop
    print("MT =",x)
    for y in range(1,13):
        print(x,'x',y,"=",(x*y))