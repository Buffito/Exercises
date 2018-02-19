import random

array=[]
check=False
past_x=[]
past_y=[]
past_z=[]
for i in range (0,30):
    array.append(random.randrange(-30,30))
    
print ("array = ",array)
print()
print()

for x in array:
    c_x=0
    c_y=0
    c_z=0
    for y in array:
        for z in array:
            if x+y+z==0:
                check=True
                for a in past_x:
                    if x==a or y==a or z==a:
                        c_x+=1
                for b in past_y:
                    if x==b or y==b or z==b:
                        c_y+=1
                for c in past_z:
                    if x==c or y==c or z==c:
                        c_z+=1
                if c_x<1 or c_y<1 or c_z < 1:
                    print (x," + ",y," + ",z, " = 0")
                    past_x.append(x);
                    past_y.append(y);
                    past_z.append(z);
                  
if (check != True):
    print ("No combination that equals zero was found!")





