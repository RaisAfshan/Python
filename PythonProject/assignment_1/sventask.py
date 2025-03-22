num = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda x: x%2 == 0, num)
print("even no. --> ",list(even))

odd = filter(lambda x: x%2 != 0 , num)
print("odd no. --> ",list(odd))