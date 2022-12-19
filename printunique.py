f=open("names.txt","rt")
un=[]
name=[]
for line in f.readlines():
    names=line.strip().split("\n")
    name.append(names)
for x in name:
    if x not in un:
        un.append(x)
un.sort()
print(un)
f.close()
