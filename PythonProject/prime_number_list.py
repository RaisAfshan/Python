
def prime_filter(list1):
    prime=[]
    for num in list1:
        if num>1:
            for i in range(2,int(num**.5)+1): #for else: if loop is completed then only else will work
                if num%i == 0:
                    break
            else:
                prime.append(num)
    return prime

print(prime_filter([1,2,3,4,5,6,7,8,9,10,11]))
