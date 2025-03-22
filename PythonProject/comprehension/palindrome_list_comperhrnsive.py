list1 = ["malayalam","aba","john","mom","1001"]

list2 = [i for i in list1 if i==i[::-1]]
print(list2)

list3 = [101,444,456,890,898]
list4 = [i for i in list3 if str(i) == str(i)[::-1]]
print(list4)