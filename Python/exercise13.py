import re
a = open("E:\\emails.txt", "r") 
f1 = a.read()
x = re.findall(r'(\w(?:[-.+]?\w+)+\@(?:[a-zA-Z0-9](?:[-+]?\w+)*\.)+[a-zA-Z]{2,})', f1) 
for j in x:
	print(j)