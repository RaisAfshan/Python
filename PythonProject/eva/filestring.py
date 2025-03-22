file1 = open(r'C:\Users\slim5\Desktop\file2.txt','r')

d=dict()
for line in file1:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

print(words)

for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1

print(d)

file1.close()