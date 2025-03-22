#1. perfect number eg: 6=1+2+3 where 1,2,3 are factors of 6 ,exclude 6 itself. ie, perfect number

# n=6
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("yes")
# else:
#     print("no")


#2. Abundent Number: here sum of the factors is greater than the no. itself eg:12 nte factors1,2,3,4,6=16>12
# n=12
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
#
# if sum>n:
#     print("abundent no.")
# else:
#     print("not ")

#3. deficent no:oppsite of abundent no. ie. sum of factors is less than no. itself

n=21
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum<n:
    print("it is deficent number")
else:
    print("it is not")
