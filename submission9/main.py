import re

string = input("Enter a string: ")
print(re.sub(r'\s+', ' ', string))
