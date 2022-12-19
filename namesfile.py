f=open("names.txt","wt")
while True:
    name=input("enter the names")
    if name=='end':
        break
    f.write(name+"\n")
