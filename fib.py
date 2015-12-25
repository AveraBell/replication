k=int(input())
f=[0,1]
b=0
for x in range (1,k):
    b=k-1
    for i in range (0,1):
        n=f[0]+f[1]
        f[0]=f[1]
        f[1]=n
print (f[k-b])
