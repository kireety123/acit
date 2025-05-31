# palindrome or not
number=int(input("Enter the Number"))
rev=0
num=number
while number>0:
    rem=number%10
    rev=rev*10+rem
    number//=10
if num==rev:
    print("it is a palindrome")
else:
    print(rev , "is not a palindrome ") 

# tables
number=int(input("enter the number"))
i=0
while i<10:
    
    i=i+1
    table=number*i
    print(number, "*", i, "=", table ) 
#factors
number=int(input("enter the number"))
i=1
count=0
while  i<=number:
    if number%i==0:
        count=count+1
    i+=1 
#for prime numbers    
if count==2:
    print("it is prime number") 
else:
    print("it is not a prime number") 



