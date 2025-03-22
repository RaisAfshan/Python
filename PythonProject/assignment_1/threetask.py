def sum(num):
    if not num:
        return 0# checks list empty , if empty sum = 0
    else:
        return num[0] + sum(num[1:])

print("sum of list -->",sum([1,2,3,4,5,6]))