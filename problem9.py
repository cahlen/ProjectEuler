'''
Project Euler Problem 9

There exists exactly one pythagorean triple where a < b < c, and a+b+c = 1000 and a^2+b^2=c^2.  Find the product abc.

Created on Dec 18, 2014

@author: cahlen
'''

for a in range(0,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            # make sure conditions are satisified 
            if ((a + b + c) == 1000) and (a < b) and (b < c) and (a != 0) and (b != 0) and (c != 0) and ((a**2 + b**2) == c**2):
                print("a: %d, b: %d, c: %d") %(a,b,c)
                print("The sum a+b+c = %d") %(a+b+c)
                print("The product abc = %d") %(a*b*c) # print result
                break