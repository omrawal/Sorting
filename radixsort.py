# 121 042 300
def converttostr(input_seq, seperator):
   final_str = seperator.join(input_seq)
   return final_str
print("Enter the number of entries radix")
n=int(input())
print("enter the entries in three digit")
a=[]
for i in range(n):
    a1=list(input())
    a.append(a1)
for j in range(0,n-1):
    for i in range(0,n-1):
        if(a[i][-1]>a[i+1][-1]):
            a[i],a[i+1]=a[i+1],a[i]
for j in range(0,n-1):
    for i in range(0,n-1):
        if(a[i][-2]>a[i+1][-2]):
            a[i],a[i+1]=a[i+1],a[i]
for j in range(0,n-1):
    for i in range(0,n-1):
        if(a[i][-3]>a[i+1][-3]):
            a[i],a[i+1]=a[i+1],a[i]
print ("the radix sort :")
print (a)
seperator = ''
for i in a:
    print(converttostr(i, seperator)+",",end=""),