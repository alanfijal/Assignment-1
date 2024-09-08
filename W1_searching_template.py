#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Insert all your names here

"""

import random, time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import W1_sorting_template


def sorting_algorithm( unsorted_array ):
    
   n = len( unsorted_array )
   sorted_array = np.copy( unsorted_array)

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 
   sorted_array = W1_sorting_template.insertionsort(sorted_array)
   
   
   

   return sorted_array


def linear_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """
    start_time = time.process_time()
    for i in range(len(array) - 1):
        if array[i] == x:
            index = i
    
    cpu_execution_time = time.process_time() - start_time
    
    # return the position of x in the array,
    # return -1 if not present
    return (index, cpu_execution_time)


def binary_search(array, x):
    
    start_time = time.process_time()
    index = -1 
    
    """
    Insert your code here

    """ 
    
    l, r = 0, len(array) - 1 #set two pointers, left at the beginning, right at the end
    
    while l != r:
        
        mid = (l + r) //2 #compute the middle index
        
        if array[mid] == x: #case if the value searched is at the middle index
            index = mid
            break
        elif x < array[mid]: #case if the value searched is smaller than the value at the middle index
            r = mid - 1
        else: #case if the value searched is greater than the value at the middle index
            l = mid + 1
    
    if array[l] == x:
        index = l
    
    cpu_execution_time = time.process_time() - start_time
    # return the position of x in the array,
    # return -1 if not present
    return (index, cpu_execution_time)


#----------------------------
# Main 

#Generate 10 random numbers between 1 and 100
random_array = np.random.randint( 1, 100, size=10)
size = len( random_array )

# Sorting the random array
sorted_array = sorting_algorithm( random_array )

# Generating a random item to be searched
x = np.random.randint( 0, 100 )

# Execute the linear search returning the position of x or -1 if not present
idx_ls = linear_search( sorted_array, x )

if idx_ls != -1:
    print("Item", x, "is present at index ", idx_ls)
else:
    print("Element", x, "is not present")

# Execute the binary search returning the position of x or -1 if not present
idx_bs = binary_search( sorted_array, x )

if idx_bs != -1:
    print("Item", x, "is present at index ", idx_bs)
else:
    print("Element", x, "is not present")


