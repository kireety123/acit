'''list is sequential data type, it arranges in order ,it provides indexes,it is enclosed in 
square brackets . it can also carry out heterogeneous data types.it is mutable, it contains dup's
   '''

list1=[1,2,3,4,5,6]
#or 
l2=list((1,2,3,4,5))
#or
l3=[]
l4=['python','java','html']
#print(l4)

#slicing
list2=list1[0:3]
#print(list2)
list1[1]=9
#print(list1)
#list1[2:5]=[7]
#print(list1)
list1[2]=[100,101,102]
#print(list1)

#concatenation and representation

l5=[1,2,3]
l6=[4,3,5]
print(l5+l6)
print(l5*2)

#list traversal
l8=[1,2,3,4,5]
for i in range(len(l8)):
    print(l8[i])
#for not using range
for i in l8:
    print(i)

#while(sir said to do this)
i=0
while i<len(l8):
    print(l8[i])
    i+=1 
#adding element
#1.append
#2.insert
#3.extend
#4.copy

#append
l9=[1,2,3,4,5]
#l9.append(9)#it will directly add number in last but only single value
#print(l9) 

#extend
l9.extend([18,19,20])
print(l9)

#insert
l9.insert(4,28)#it will take the index of number and replace it
print(l9)

#copy
l10=l9.copy()#it will store a copy

#removing elements

#pop
l11=[1,2,3,4,5]
l11.pop()
print(l11)#it will remove the last element by default
l11.pop(1)#here 1 is nothing but index 
print(l11)

#remove
l11.remove(1)#here 1 is value not index , it only remove 1 value not multiple if exists.
print(l11)


#clear
l11.clear()
print(l11)#it will clear the data and gives empty set

#del
del(l11)
#print(l11)# it will say l11 is not defined due to the above command


#task
list12=['kireety','kittu','veera','venkata','satya','sai']


print(list12[0:4])

list12[0:3]=["apple"]#["apple","venkata","satya","sai"]
print(list12)
list12[0:3]="apple"#["a","p","p","l","e","venkata","satya","sai"]

list13=["virat","rohit","dhawan"]
#list13[0]=["kapildev","yuvraj","zaheerkhan"]
#print(list13)#[['kapildev', 'yuvraj', 'zaheerkhan'], 'rohit', 'dhawan']
list14=["dhoni","kl rahul","pant"]

list15=list13+list14
#print(list15)#['virat', 'rohit', 'dhawan', 'dhoni', 'kl rahul', 'pant']

print(list13*3)#['virat', 'rohit', 'dhawan', 'virat', 'rohit', 'dhawan', 'virat', 'rohit', 'dhawan']

#for x in list15:
    #print(x)#virat
#rohit
#dhawan
#dhoni
#kl rahul
#pant

#for x in range(len(list15)):
    #print(list15[x])# it is printing

#i=0
#while i<len(list15):
    #print(list15[i])
    #i+=1 # it is printing

list17=list15.copy()   

#list15.append("sachin tendulkar")
#print(list15)#['virat', 'rohit', 'dhawan', 'dhoni', 'kl rahul', 'pant', 'sachin tendulkar']

list15.extend([""])





