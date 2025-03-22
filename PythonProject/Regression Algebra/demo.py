import re
#search() : Searches the entire string for the first occurrence of the pattern.
# txt = "the rain in spain"
# x = re.search("in",txt)
# if(x):
#     print("there is a match")

#findall
# txt = "the rain in spain"
# x = re.findall("ai",txt,)
# print(x)

#sub
# txt = "the rain in spain"
# x = re.sub("a","9",txt,1)
# print(x)

#split
# txt = " rain in spain"
# x = re.split("in",txt)
# print(x)

#span,group,string
# txt = "rain in spain"
# x = re.search("in",txt)

#match() : matches the pattern only  at the  beginning of the string.
txt = "hello world"
match = re.match('hello',txt)
print(match.group())# group() is a method that returns the entire match

txt1 = " the entire are match if no groups are defined"
match1 = re.search('are',txt1)
print(match1.group())

#findall():Finds all occurrences of the pattern in the string.
text = "Hello, Hello, Hello!"
pattern = r"Hello"

matches = re.findall(pattern, text)
print("All matches:", matches)

#sub():Replaces all occurrences of the pattern with a new string.
text = "I love cats. Cats are cute."
pattern = r"cats"
new_text = re.sub(pattern, "dogs", text, flags=re.IGNORECASE)
print(new_text)