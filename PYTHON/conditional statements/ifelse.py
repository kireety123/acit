#even or odd numbers
number=int(input("enter the number :"))
if number%2==0:
    print("the number is even")
else:
    print("it is odd")
#leap year
year= int(input("enter the year :"))
if year%100==0:
    if year%400==0:
        print("It is a leap year")
elif year%4==0:
    print("It is a leap year.")
else:
    print("It is not a leap year")
# life cycle in the terms of age
age =int(input("enter the age :"))
if age>=10 and age<20:
    if age<=15 :
        print("he is a school student")
    else:
        print("he is a college student")
elif age>=20 and age<30:
    if age<24:
        print("he is doing a job")
    elif age>24 and age<28:
        print("he is married")
    elif age==24:
        print("he is enjoying ")
    elif age>=28 and age<=29:
        print("he is gonna have kids")
    else:
        print("he is a father")
elif age>=30 and age<=60:
    if age>=30 and age<40:
        print("he is a father of a elementary school kid")
    elif age>=40 and age<50:
        print("he is a father of school student")
    elif age>=50 and age<=59:
        print("he is a father of college student")   
    else:
        print("he is going to retire")
elif age<10 and age>0:
    print("he is just a kid")
elif age>60 and age<=85:
    print("he is enjoying his retired life")
elif age>85 and age<=90:
    print("he is waiting for the invitation card from the death")
else:
    if age==0:
        print("he is a soul in the mother's womb")
    else:
        print("he died")



                                                 
    
