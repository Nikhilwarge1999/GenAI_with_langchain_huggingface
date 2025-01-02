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
