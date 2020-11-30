# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:44:37 2020

@author: Abhishek Maurya
"""

print("hello world")

#Numbers
#a=3 , b=5  #a and b are number objects 

#Strings

str1='Hello Abhishek.'
str2='How are you?'
print(str1[:])
print(str1[6:-1])
print(str1*2)
print(str1+" "+str2)

#Lists
l  = [1, "Hello", "Python", 3.7] 
print (l[3:])  
print (l[0:2])
print (l);  
print (l + l);  
print (l * 3);
print (type(l))

#Lets try mutation 
l[1] = "Bye"
print (l)

#Tuple
t  = ("hi", "python", 2, 4)  
print (t[1:]);  
print (t[0:2]);  
print (t);  
print (t + t)
print (t * 3)  
print (type(t))
 
#Lets try mutation 
t[1] = "Bye"
print (t)

#TypeError: 'tuple' object does not support item assignment

#Dictionary
d = {1:"Jimmy", 2:'Alex', 3:'john', 4:'mike'};
print("1st name is "+d[1]);  
print("2nd name is "+ d[4]);  
print (d); 
print (d.keys());  
print (d.values());

#----ADVANCED----
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)
print(shoplist)

#run next 2 lines together
for i in shoplist:
    print(i.title(), end =',')

#add item to list
shoplist.append('rice')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0].title()
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )
zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = 'c', 'java', 'php'  #better to put (), this also works
languages

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon

student = {'20cs06001': 'Homi', '20cs06003': 'Samannay', '20cs06004':'Vikas','20cs06005':'Abhishek','20cs06010':'Aditya','20cs06011':'Ranjeet','20cs06013':'Swastik','20cs06014':'Kunal','20cs06019':'Avadesh','20cs06020':'Kojagori'}
student
student['20cs06005']
print('Name of rollno 20cs06020 is ' +student['20cs06020'])
del student['20cs06003']
student
len(student)

for rollno, name in student.items():
    print('name of roll number {} is {} '.format(rollno, name) )

#Lets test Mutation: 
#adding a value
student['20cs06017'] = 'Mukesh'
student

#Set
#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india','england','australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

#Checking whether a data value exists in a set or not.
'india' in teamA
'india' in teamB

#Adding values in a set
teamB.add('china')
teamA  #puts in order
teamA.add('india')
teamA  #no duplicates
teamA.remove('china')
teamA.sort()
#AttributeError: 'set' object has no attribute 'sort'
teamA

#Create dataframe :
import pandas as pd
 
#Create a DataFrame
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
            'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                    'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
                    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                               'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}

df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score']]

#View first two rows of the dataframe in pandas:
df[:2]
df.head(8)
df.tail(8)
