import re

#input type=text
txt="kireety varma"
print(re.fullmatch('[a-zA-Z ]+',txt))

#input type=email
email="kireety.1_23@gmail.com"
print(re.fullmatch('[a-z0-9._]+(@gmail|@outlook){1}\.com{1}',email))

#input type=password
password="Shivani@17_4_24"
print(re.fullmatch('[a-zA-Z@_0-9]{8,16}',password))

#input type=number
number='6281007463'
print(re.fullmatch('[6-9]\d{9}',number))

# input type=age
age='1'
print(re.fullmatch('[0-9]{1,2}',age))#1 to 100 where 100 is not included






