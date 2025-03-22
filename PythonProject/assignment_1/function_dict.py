def person(name,age,location,salary):
    my_dict={}
    my_dict["name"] = name
    my_dict["age"] = age
    my_dict["location"]= location
    my_dict["salary"] =salary
    for key,value in my_dict.items():
        print("key :",key ,",value :",value)

person(name="abc",age="45",location="clt",salary=25000)
#

# def person(name,age,location,salary):
#     my_dict={}
#     my_dict[name] = name
#     my_dict[age] = age
#     my_dict[location] = location
#     my_dict[salary] = salary
#     print(my_dict)
# person(name="abc",age="45",location="clt",salary=25000)


