

st = "his iam tom, iam a pyhton developers"
print("length of the string :",len(st))
print("count of the particular word: ",st.count("iam"))
print("startswith method in :" , st.startswith("hi"))
print("endswith method :", st.endswith("developer"))
print("capitilize method", st.capitalize())

st2 =  "hello world"
s1= st2[6:]
print(s1)

j1 =  "apple"
print(" ".join("apple"))

st3 ="APPLE    "
print(st3.strip())

Replace=j1.replace("apple","APPLE")
print(Replace)

print(st.index("o"))

st4 = "futura labs"
words = st4.split()
reverseWords = list(reversed(words))
reversedWords = ' '.join(reverseWords)
print(reversedWords)

st = "sky is blue"
words = st.split()
list1=[]

print(words)
for i in words:
    leng = len(i)
    list1.append(leng)
print(list1)
min_length = min(list1)
print(min_length)
words_index = list1.index(min_length)
print(words[words_index])

#1.Write a Python program to calculate the length of a string.
def string_length(str):
    count=0
    for char in str:
        count=count+1
    return count

print(string_length('hello world'))

#2.  Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
str1 = "Google"

dict  = {}

for n in str1:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
print(dict)

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

str2='heybro'
# for char in str2:
#     print(char)
if len(str2)>2:
    print(str2[0:2]+str2[-2:])
else:
    print("empty string")

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'

# str3 = 'restart'
# print(str3[0])
# word3 = input("enter the charecter: ")
# if word3 in str3:
#     x = str3.replace(word3,'$')
#     print(x)

str4= 'restart'
char = str4[0]
str4 = str4.replace(char,'$')

replaced = char+str4[1:]
print(replaced)

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'

a='abc'
b='xyz'










