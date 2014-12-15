'''
Project Euler Problem 7

Find the 10001st prime number

Created on Dec 13, 2014

@author: cahlen
'''

import math

a=1
num=2
counter = 0

while counter < 10001:
    if any(num % a == 0 for a in range(2, num)) is False:
        print("%d is prime") % num
        counter+=1
    #else:
    #    print("%d is not prime") % num
    num+=1  
        
