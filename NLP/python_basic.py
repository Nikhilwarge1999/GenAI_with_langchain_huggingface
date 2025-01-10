#how to reverse the string
n="nikhil"
print (n[::-1])
# ______________________________________________________________

# python lambda fuction
x= lambda x: x+2
print(x(12))

x= lambda x,y: x+y

# lambda using map nad without map finction
lst=[1,2,3]
d=list(map(lambda x : x**2, lst ))
# c=list(map(lambda x : lst**2, ))

print("lambda function", d)
# print("lambda function", c)
# _________________________________________________________________
# what is list  comprehsion

a =[1,2,34,5,6,4]
b=[x for x in a ]
print("this is list comprehension",*b)

# " * "argument unpack the list and print the saparate element

# Square of each number 

b = [x**2 for x in range(1,10)]
print ("square of all the element",*b)

# printing the even numbers



x =[x for x in range(1, 10) if x %2 ==0]
print ("even numbers are",*x)


# print words which has more alphabets 

words = ["apple", "to", "cat", "elephant", "dog"]

# list take index form 0
d=[x for x in words if len(x) > 3]
print("length of word more than 3", *d)

# 2D to 1D

matrix = [[1, 2, 3], [4, 5, 6]]

mat=[row  for col in matrix for row in col ]
print("change to matrix ", *mat)

# Swap elements in a tuple for a list of tuples.

parse=[('a',1),('b',2)]

g=[(x,y) for y,x in parse]
print("swaped element",*g)

# Transform all characters in a string to uppercase

text="nikhil"

t=[chr.upper() for chr in text]

print("upper case later ", t)
print("upper case later ", *t)

# arthmetic opartion 

mul=[x*10 for x in range(1, 10)]
print("multipal of 10", *mul)

# converting str to int

strings = ['10', '20', '30']

f=[int(x) for x in strings]
print("str to int type casting",f)


# generate random nonloc
import random

ran_int=random.randint(1,10)
ran_float=random.uniform(1,10)
ran_range=random.randrange(1,10,4)

print("randon number is ",ran_int)
print("randon number is ",ran_range)
print("randon number is ",ran_float)

# random number usig numpy

import numpy as np

rnad= np.random.randint(1,10)
print("rnadom int using numpy",rnad)

# check all char id aphanumic or not 

a= "hell1*232"

b=[x.isalnum() for x in a] #list comprehinsion

print("numeric",b)

# how to join words form list

words = ['Hello', 'World', 'Python']
print(''.join(words))

# how to remove leading white spaces

words = "Hello, World, Python"

print(words.lstrip())


# string
x=lambda x: x**2

print("square is", x(2))

# list
a=[1,2,3,4,5]
f=list(map(lambda x:x**2, a))
print(f)

# how to converthr str to list 
a="nikhil"

b=a.split(" ")
print(b)

# reverse string without using for loop

str1 = "Analytics Vidhya"
str2=""
for i in str1 :
    str2= i + str2
    print(str2)

# sort list
my_list = [3, 2, 1]
# my_list.remove()
my_list.pop(1)
print(my_list)

import numpy as np

arr1= np.array([1,2,3,4,5])
print(type(arr1))
arr2= arr1[::-1]
print(arr2)
print("reverse uing flip method",np.flip(arr1))

print("delete emlement",np.delete(arr1, 2))

lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']
lis3=[x+y for x, y in zip(lst1, lst2) ]
#join 2 list by index
print(lis3)

# square of every element present in the list

lst = [1, 2, 3, 4]
b=[x**2 for x in lst ]
print(b)    

lst = [1, 2, 3, 4]
lst_final = []
for x in lst:
    lst_final.append(x * x)
print(lst_final)

c=[1,2,3,4]
x=lambda y: y**2, c

c=['a','b','c']
print(''.join(c))

# remove extra white space using strip()

s = '   Hello, World!   '

print(s.strip())

# prime no or not 

from math import sqrt

def prime_or_not(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return 0
    return 1
if prime_or_not(4):
    print("prime number ")
else:
    print("not prime number")



#  need to check if prime or not 

def prime(num):
    if num <= 1:  # Check if number is <= 1
        print("Enter a number greater than 1.")
        return False
    
    # Check divisibility from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Not prime if divisible by i
    
    return True  # Prime if no divisors are found


# User Input
# p = int(input("Enter a number: "))

# Check if the number is prime
# if prime(p):
    # print(f"{p} is a Prime number.")
# else:
    # print(f"{p} is NOT a Prime number.")


# how to swap value in variable

a=10
b=20

a,b =b,a
print("a",a)
print("b",b)

# Write a program in Python to return the factorial of a given number using recursion.

def factorial(n):
    if n== 1 :
        return n
    else:
        #n*(n-1)
        return n * factorial(n-1)
print(factorial(5))

# --------------------------------------
import math

fact=int(input("enter the value"))
print(math.factorial(fact))

# Write a code to convert a list of characters to a string of characters separated by a comma

li=['a','b','c']

re=','.join(map(str,li))
print(*li,"this is ")

print(type(re))
print(type(li))


reverse=input("enter any valu")
# with list
# new_reverse=int(reverse[::-1])
# without list
lis=''

for i in reverse:
    lis=i+lis
lis=int(lis)
print("new reverse is without list i s",lis)
# print("reverse string is ",new_reverse)
# print(type(new_reverse))
print(type(lis))


armstrong=input("enter any number ")
armstrong=armstrong.split(',')
 
y=[x*3 for i in armstrong]



