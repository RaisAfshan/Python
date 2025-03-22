def func(n):
    return lambda x:x*n
multiply = func(3);
print(multiply(7));


mylist = [1,2,3,4,5,6,7,8,9]
even_num = list(filter(lambda x: x%2 == 0, mylist)) #my_list argument and x is parameter so, my_list is passed to parameter x
print(even_num)