#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Insert all your names here

"""

import random, time
import matplotlib.pyplot as plt
import numpy as np


def bubblesort( unsorted_array ):

    n = len( unsorted_array )
    #Create a copy of the unsorted array so to not modify it
    #and modify the sorted_array only
    sorted_array = np.copy( unsorted_array)

    """
    Insert your code here

    """ 

    #Return the sorted array
    return sorted_array


def insertionsort( unsorted_array ):

    n = len( unsorted_array )   
    #Create a copy of the unsorted array so to not modify it
    #and modify the sorted_array only
    sorted_array = np.copy( unsorted_array)

    """
    Insert your code here

    """ 
    
    #Return the sorted array
    return sorted_array



#----------------------------
# Main 

#Generate 10 random numbers between 1 and 10000
random_array = np.random.randint( 1, 10000, size=10)
size = len( random_array )

#Ordering from smallest to largest using Bubble sort
bubble_array = bubblesort( random_array )

#Ordering from smallest to largest using Insertion sort
insertion_array = insertionsort( random_array )

# Print the results
print( "\n Unsorted array of", size, "elements is:\t\t", random_array )
print( "\n Bubble sorted array of", size, "elements:\t\t", bubble_array )
print( "\n Insertion sorted array of", size, "elements:\t", insertion_array )

