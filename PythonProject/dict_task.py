#add key value to dict
car = {"brand":"ford","model":"mustang","year":1964}

car["color"] = "red"
print(car)

#print the value
print(car["model"])

#find minimum value
mark = {"physics":75,"maths":55,"history":79}
temp = min(mark.values())
print(temp)
for key,value in mark.items():
    if(value == temp):
        minimum = key;
print(minimum)

mark1 = {"physics":90,"maths":78,"chemistry":78}
temp1 = min(mark1.values())
print(temp1)
minimum1 =[];

for key,value in mark1.items():
    if(value == temp1):
        minimum1.append(key)
print(minimum1)

#object of object
sample = dict({"emp1":{"name":"john","salary":7500}, "emp2":{"name":"emma","salary":8000},"emp3":{"name":"brad","salary":500}})
# sample["emp1"]["salary"] = 8500
print(sample)

sample["emp1"]["salary"] = 8500
# for key,value in sample:
#     print(value)

print(sample)
