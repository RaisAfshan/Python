dict1 = {"one":"anu","two":"john","three":"lanny"}
dict2 = {k:v.upper() for (k,v) in dict1.items()}
print(dict2)

dict3 ={k.upper() for k in dict1.values()}
print(dict3)

dict4 ={k.upper() for k in dict1.keys()}
print(dict4)