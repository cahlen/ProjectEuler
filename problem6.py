'''
Project Euler Problem 6

Find the difference between the square of the sum of the first 100 natural numbers, and the sum of the 
squares of the first 100 natural numbers.

Created on Dec 13, 2014

@author: cahlen
'''

import math

x,y=1,1
a,b=0,0

# Sum the square of natural numbers from 1 ... 100
for x in range(1,101):
    a+=x**2

# Sum of natural numbers from 1 ... 100
for y in range(1,101):
    b+=y
    
# Square sum from above loop
b=b**2

# Print the difference
print(b-a)

   
   
