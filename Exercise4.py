roman=[(1000000,"̅M̅"),(500000,"̅D̅"),(100000,"̅C̅"),(50000,"̅L̅"),(10000,"̅X̅"),(5000,"̅V̅"),(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]



n=int(input("Insert an integer between 1 and 1000000!"))

def int2rom(n):
    
    rom=""

    while n>0:
        for i,r in roman:
            while n>=i:
                rom+=r
                n=n-i
    return rom

print (int2rom(n))
