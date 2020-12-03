# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:26:13 2020

@author: Abhishek Maurya
"""
"""
for loop is used in case where we need to execute some part of the code until the given condition
is satisfied. It is better to use for loop if the number of iteration is known in advance.
It is frequently used to traverse the data structures like list, tuple, or dictionary.
"""
#Example 1

for i in range(1,11):
    print(i,end=" ")
    
#Example 2 printing the table of a given number
n=int(input("Enter a number: "))
for i in range(1,11):
    print("%a X %a=%a"%(n,i,n*i))
    

#Example 3:Nested For loop
n=int(input("Enter the number of rows you want to print:"))
for i in range(n+1):
    print()
    for j in range(i+1):
        print("*",end=" ")
        
#Example 4: Else statement with For loop
for i in range(0,5):
    print(i)
else:print("for loop completely exhausted, since there is no break.")

"""
while loop is to be used in the scenario where we don't know the number of iterations in advance. 
The block of statements is executed in the while loop until the condition specified in while loop 
is satisfied.
"""

#Example 5

i=1
while i<=10:
    print(i,end=" ")
    i+=1

"""    
-------Elif Statement------------------
The elif statement enables us to check multiple conditions and execute the specific block of 
statements depending upon the true condition among them.It works like if-else-if ladder statement.
"""
#Example:
number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50");
elif number==100:
    print("number is equal to 100");
else:
    print("number is not equal to 10, 50 or 100");



