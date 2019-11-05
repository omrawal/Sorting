# no of inputs 8
# inputs 9,8,3,7,5,6,4,1
print("Welcome to shell sort")
a=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    k=int(input())
    a.append(k)
while(n>0):
    p=n//2
    for i in range(0,p):
        if(a[i]>a[i+p]):
            a[i],a[i+p]=a[i+p],a[i]
    n=n//2
print("The sorted list is: ")
print (a)