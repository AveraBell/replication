a=input()
b=0
for i in range (0, len(a)):
    if a[i]=="T":
        a=a.replace('T','U')
print (a)
