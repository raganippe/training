# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:53:06 2015

@author: AGAN26R
"""

# Affectations
x,y,z = 1,2,3
print x
print y
print z


# Boucles
for i in [1,2,3,4,5,6]:
    print "The value of i is ",i," ..."

for value in range(50):
    print "My value is", value
    
x = 10
while x >= 0:
    print "x is still not negative.", x
    x = x-1    
    
# saisies    
    
n = raw_input("What's your name ?")
print "Hello ", n

n = input("What's your age ?")
print "So you are ", n, " years old"
