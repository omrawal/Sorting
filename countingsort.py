print("Welcome to counting sort")
r1=int(input("Enter the lower bound of range "))
r2=int(input("Enter the upper bound of range "))
a = {i: 0 for i in range(r1,r2)}
b=[]
n=int(input("Enter the number of inputs"))
for i in range(0,n):
    k=int(input())
    b.append(k)
for i in b:
    a[i]+=1
for i in range (0,r2-1):
    a[i+1]=a[i+1]+a[i]
a1 = {i: 0 for i in range(0,r2-r1)}
for i in range(0,len(b)):
    a1[a[b[i]]-1]=b[i]
    a[b[i]]-=1
print(a1)
