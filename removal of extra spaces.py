import re
f=open('names.txt','rt')
for line in f.readlines():
    res = re.sub(' +', ' ', line)
    print(res)
f.close()