a=input()
k=len(a)-1
for i in range(0,len(a)):
    if a[i]=="A":
        a=a.replace('A','B')
for i in range(0,len(a)):
    if a[i]=="T":
        a=a.replace('T','A')
for i in range(0,len(a)):
    if a[i]=="G":
        a=a.replace('G','D')
for i in range(0,len(a)):
    if a[i]=="C":
        a=a.replace('C','G')
for x in range(0,len(a)):
    if a[x]=="B":
        a=a.replace('B','T')
for x in range(0,len(a)):
    if a[x]=="D":
        a=a.replace('D','C')
s=a[len(a):0:-1]+a[0]
print (s)
