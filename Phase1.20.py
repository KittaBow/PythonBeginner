#exchange money and number of banknotes

#2000 => 1000 => 2 bills
#1800 => 1000 => 1 bill, 500 => 1 bill, 100 => 3 bills

number = int(input("amount of money: "))

# amount
if number>=1000:
    print("1000 bath = ", number//1000,"bills")
    number = number % 1000 #1500 หารเอาเศษ 1000 = 500

if number>=500:
    print("500 bath =", number//500,"bills")
    number = number % 500

if number>=100:
    print("100 bath =", number//100,"bills")
    number = number % 100

if number>=50:
    print("50 bath =", number//50, "bills")
    number = number % 50

if number>=20:
    print("20 bath =",number//20, "bills")
    number = number % 20
    

