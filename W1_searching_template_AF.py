#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Insert all your names here

"""

import random, time
import matplotlib.pyplot as plt
import numpy as np


def sorting_algorithm( ):
    

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 

   
   result_insertion = {}
   for i in range(1000, 10000, 1000):
       random_array = np.random.randint( 1, 100, size=i)
       _, exec_time = insertion_sort(random_array)
       result_insertion[i] = exec_time
    
   plt.plot(result_insertion.keys(), result_insertion.values())
   plt.show()


   










def insertion_sort(unsorted_array):
    n = len( unsorted_array )
    sorted_array = np.copy( unsorted_array)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and sorted_array[j + 1] < sorted_array[j]:
            tmp = sorted_array[j + 1]
            sorted_array[j + 1] = sorted_array[j]
            sorted_array[j] = tmp
            j -= 1
    
    cpu_execution_time = time.process_time()
    print(cpu_execution_time)
    return sorted_array


  




def linear_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """

    for i in range(len(array) - 1):
        if array[i] == x:
            index = i

    
    # return the position of x in the array,
    # return -1 if not present
    return index


def binary_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """ 
    l, r = 0, len(array-1)

    while l != r:
        mid = l + r // 2
        if x < array[mid]:
            r = mid - 1
        else:
            l = mid

    if array[l] == x:
        return l
    else:
        return -1 
    
    # return the position of x in the array,
    # return -1 if not present
    return index


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


