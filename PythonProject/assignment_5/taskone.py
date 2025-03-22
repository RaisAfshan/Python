import re
txt = "ronaldo scored 4 goal in a match"
x = re.findall(r"\d",txt)
print(x)