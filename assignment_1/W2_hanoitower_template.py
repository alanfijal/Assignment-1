#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 

@author: 
Alan Bruno Fijal, Maria Fiamenghi, Marc Farras, Patricia Cerda

    
"""

#Function to solve the Hanoi Tower of n elements and moving the disks from rod source
# to rod destination making use of the auxiliary rod
def hanoitower( n, source, destination, auxiliary ):
         
    """
    Insert your code here

    """ 
    if n == 1:
        print("Disk {} moves from {} to tower {}".format(n, source, destination))
        return 

    hanoitower(n-1, source, destination, auxiliary)
    print("Disk {} moves from {} to tower {}".format(n, source, destination))
    hanoitower(n-1, auxiliary, source, destination)
    
    


    
# Main

# Define the number of disks
n = 3
print( "The movements required to solve the Hanoi Tower with", n, "disks are:")

# Call the recursive algorithm
hanoitower( n, 'Rod 1', 'Rod 3', 'Rod 2' )



