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

    sorted_array = np.copy( unsorted_array)
    right = False
    
    while not right:
        swaps= 0
        for i in range(n-1):
            if sorted_array[i]>sorted_array[i+1]:
                sorted_array[i], sorted_array[i+1] = sorted_array[i+1], sorted_array[i]
                swaps += 1
                
        if swaps == 0:
            right = True

    #Return the sorted array
    cpu_execution_time = time.process_time()
    return cpu_execution_time, sorted_array


def insertionsort( unsorted_array ):

    n = len( unsorted_array )   
    #Create a copy of the unsorted array so to not modify it
    #and modify the sorted_array only
    sorted_array = np.copy( unsorted_array)

    right = False
    
    while not right:
        for i in range(1, n):
            key = sorted_array[i]
            j = i - 1
            while j >= 0 and key < sorted_array[j]:
                sorted_array[j + 1] = sorted_array[j]
                j -= 1
            sorted_array[j + 1] = key
    
    #Return the sorted array
    cpu_execution_time = time.process_time()
    return cpu_execution_time, sorted_array



#----------------------------
# Main 

#Generate 10 random numbers between 1 and 10000
random_array = np.random.randint( 1, 10000, size=10)
size = len( random_array )

#Ordering from smallest to largest using Bubble sort
bubble_array = bubblesort( random_array )

#Ordering from smallest to largest using Insertion sort
insertion_array = bubblesort( random_array )

# Print the results
print( "\n Unsorted array of", size, "elements is:\t\t", random_array )
print( "\n Bubble sorted array of", size, "elements:\t\t", bubble_array )
print( "\n Insertion sorted array of", size, "elements:\t", insertion_array )

