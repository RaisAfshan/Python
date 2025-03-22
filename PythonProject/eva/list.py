n = [10,20,30,40,50,60,70,80,90,100]
i=0
while i<len(n):
    if n[i] > 50:
        n.pop(i)
    else:
        i=i+1
print(n)

