
str3='   welocme to python'
r=str3.replace(' ','*')
print(r)
print(len(str3))
x1=str3.lstrip()
print(len(x1))

# replace
str4='a,b,c,d'
r1=str4.replace(',','-',2)
print(r1)

# join 
s1='Ganesh'
s2='I am from tenali'
out=s1.join(s2)
print(out)

# startswith
s3='Python is simple'
out1=s3.startswith('Python is')
print(out1)

# endswith
out2=s3.endswith('e')

# removeprefix
out3=s3.removeprefix('Python ')
print(out3)
# removesufix
out4=s3.removesuffix('e')

# partisiton
s4='kireety@gmail.comsurya@gmail.com'
_1=s4.partition('@')
print(_1)
_2=s4.rpartition('@')
print(_2)
      