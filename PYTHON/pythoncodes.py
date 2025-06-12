# voting
age=int(input("enter the age"))
if age>=18:
    print("he is eligible to vote")


#even or odd        

num=int(input("enter the number"))
if num%2==0:
    print("it is even")
else:
    print("it is a odd number") 

#grade

marks=int(input("enter the marks"))
if marks>=90:
    print("grade of the student is A")
elif marks>=75:
    if marks<90:
        print("grade of the student is B")
elif marks>=60:
    if marks<75:
        print("grade of the student is C")
elif marks>=50:
    if marks<60:
        print("the grade of the student is D")
else:
    if marks<50:
        print("the student is fail")    


#16th numbers from 1 to 10
# using while loop 
i=0
while i<10:
    i+=1
    print(i)

#using for loop
i=1
for i in range(1,11):
    print(i)
#sum of even numbers in given range 
#using while loop
evnum=int(input("enter the range"))
i=1
count=0
while i<evnum:
    if i%2==0:
       count=count+i
    i+=1   
print(count)
#using for loop
count=0
for i in range(evnum):
    
    if i%2==0:
        count=count+i
print(count)

#triangle pattern
n=5
for i in range(1,n+1,1):
    print(" "*(n-i)+"* "*i)  


#leap years
for year in range(2000,3001):
    if year%100==0:
        if year%400==0:
            print("it is a leap year")
        else:
            print("it is not a leap year")

    elif year%4==0:
        print("it is a leap year")
    else:
        print("it is not a leap year")
#string methods



   



