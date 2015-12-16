n=int(input())
k=int(input())
x=1
y=0
c=0
for i in range (1,n):
    c=x
    x=x+y
    y=k*c
print (x)
