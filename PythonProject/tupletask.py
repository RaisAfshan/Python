t = (1,2,3)
x,y,z= t

print(" x:",x," y:",y," z:",z)

#swap two tuples

tuple1  = (11,12)
tuple2 = (99,88)

tuple1 , tuple2 = tuple2 , tuple1

print("tuple1 : ", tuple1)
print("tuple2 :", tuple2)

#copy the particular item from a tuple
t1 = (11,22,33,44,55)
new_tuple = t1[-2:]
print(new_tuple)