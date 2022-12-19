lines=[]
with open("names.txt",'rt') as f:
    for line in f.readlines():
        name = line.strip().split("\n")
        lines.append(name)
print(lines)
with open ("temp.txt", 'wt') as f:
      f.write(line+'\n')