name="test.txt"
f=open(name)

#print(f.readline())
for line in f:
    if 'to' in line:
        print(line)
f.close()