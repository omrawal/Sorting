#26 39 68 78 12 21 72 17 94 23
def converttostr(input_seq, seperator):
   final_str = seperator.join(input_seq)
   return final_str
print("Enter the number of entries bucket")
n=int(input())
print("enter the entries in range 1-100")
a=[]
for i in range(n):
    a1=int(input())
    a.append(a1)
b0=[]
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
b7=[]
b8=[]
b9=[]
for i in a:
    if(0<=i<=9):
        b0.append(i)
        b0=sorted(b0)
    elif(10<=i<=19):
        b1.append(i)
        b1=sorted(b1)
    elif(20<=i<=29):
        b2.append(i)
        b2=sorted(b2)
    elif(30<=i<=39):
        b3.append(i)
        b3=sorted(b3)
    elif(40<=i<=49):
        b4.append(i)
        b4=sorted(b4)
    elif(50<=i<=59):
        b5.append(i)
        b5=sorted(b5)
    elif(60<=i<=69):
        b6.append(i)
        b6=sorted(b6)
    elif(70<=i<=79):
        b7.append(i)
        b7=sorted(b7)
    elif(80<=i<=89):
        b8.append(i)
        b8=sorted(b8)
    elif(90<=i<=100):
        b9.append(i)
        b9=sorted(b9)
    else:
        print("out of range")
b=[]
if(len(b0)!=0):        
    b.append(b0)
if(len(b1)!=0):        
    b.append(b1) 
if(len(b2)!=0):        
    b.append(b2)
if(len(b3)!=0):        
    b.append(b3)
if(len(b4)!=0):        
    b.append(b4)
if(len(b5)!=0):        
    b.append(b5)
if(len(b6)!=0):        
    b.append(b6)
if(len(b7)!=0):       
    b.append(b7)
if(len(b8)!=0):
    b.append(b8)
if(len(b9)!=0):
    b.append(b9)
sorted(b)
seperator = ''
print("The sorted list by bucket sort is")
for i in b:
    print(converttostr(str(str(i)), seperator)+",",end="")