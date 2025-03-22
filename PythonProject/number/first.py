# n = 268
# m=n # c\we are copying n into m because when we need to compare this to n , n will not be zero

# while m != 0:
#     d = m%10
#     print(d)
#     m=m//10

#1.Palindrome:
# n= 282
# m=n
# sum = 0
# while m!=0:
#     d=m%10
#     sum = sum* 10+ d
#     m=m//10
# if sum == n:
#     print("it is palindrome")

#2.spynumber
# n=123
# m=n
# sum=0
# prod=1
#
# while m!=0:
#     d=m%10
#     sum = sum +d
#     prod = prod * d
#     m=m//10
#
# if prod == sum:
#     print("it is a spy number")
# else:
#     print("it is not a spy number")

#3.special number
# n=59
# m=n
# sum=0
# prod=1
# while m!=0:
#     d=m%10
#     sum = sum+d
#     prod = prod*d
#     m=m//10
#
# if (sum+prod)==n:
#     print("special number")
# else:
#     print("not s special number")

#4.harshad number or niven number 156=1+5+6=12 156 is divisible by 12
# n=156
# m=n
# sum=0
# while m!=0:
#     d=m%10
#     sum=sum+d
#     m=m//10
# if(n%sum==0):
#     print("this is a niven number")

#5. Duck Number: number that has zero in it eg:120,407
# n=40700
# m=n
# count=0
# while m!=0:
#     d=m%10
#     if d==0:
#         count=count+1
#     m=m//10
# if count>0:
#     print("it is duck no.",count)
# else:
#     print("not duck number")

#6.neon number:eg:9,9*2=81,8+1=9
# n=9
# sum=0
# m=n*n
# while m!=0:
#     d=m%10
#     sum=sum+d
#     m=m//10
# if sum==n:
#     print("it is neon number")
# else:
#     print("it is not a neon number")

#7. Automorphic number: is number whic contained in last digit of its square eg:25=625
n=25
m=n
flag=0
q=n*n
while m!=0:
    d=m%10
    d1=q%10
    if d==d1:flag=1
    m=m//10; q=q//10
if flag==0:
    print("yes")
else:
    print("no")



