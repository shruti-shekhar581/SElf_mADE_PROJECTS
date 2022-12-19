import os
startdir=r'c:\users\shruti\PycharmProjects\may17\filesdemo'
allentries=os.walk(startdir)
count=0
for (dirname,folder,files) in allentries:
    for file in files:
        if file.endswith(".py"):
            print(dirname +'\\'+file)
            count+=1
print(count)