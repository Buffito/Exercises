n=int(input("Insert number of digits...\n"))
s=int(input("Insert Sum...\n"))

Max=int(n*"9")
Min=10**(n-1)
print ("max: ", Max , "|| min: ", Min)
final=[]
count=0

for i in range (Min,Max+1):
    num_str=str(i)
    num_list=list(num_str)
    
    check=True

    for j in range (0,n-1):
        if int(num_list[j])>=int(num_list[j+1]):
            check=False

    if check==True:
        s1=0
        for j in range (0,n):
            s1+=int(num_list[j])
        if s1==s:
             final.append(i)
             count+=1

print ("====================================")             
print ("====================================")

print ("The numbers with ", n, " digits and sum ", s, " are: \n")
for i in range (0,count):
    print (final[i])
    
#Test for n=3 s=6 --> 123
#Test for n=5 s=15 --> 12345
