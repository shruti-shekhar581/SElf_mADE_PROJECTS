f=open("names.txt","rt")
l=set()
for line in f.readlines():
    name=line.strip().split("\n")
    l.update(name)

for obj in l:
    print(obj)
