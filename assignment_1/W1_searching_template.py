#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Insert all your names here
Alan Bruno Fijal, Maria Fiamenghi, Marc Farras, Patricia Cerda
"""

import random, time
import matplotlib.pyplot as plt
import numpy as np
import W1_sorting_template


def sorting_algorithm( unsorted_array ):
    
   n = len( unsorted_array )
   sorted_array = np.copy( unsorted_array)

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 
   sorted_array = W1_sorting_template.insertionsort(sorted_array) #perform sorting, using the imported insertionsort from the sorting template
   return sorted_array #return sorted array


def linear_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """
    sorted_array = sorting_algorithm(array) #sort the array
    for i in range(len(sorted_array) - 1): #traverse through the array
        if sorted_array[i] == x: #if the value at the current index is equal to the searched value
            index = i #set the index to the cur value of the pointer
            break #break the loop
    
    

    
    # return the position of x in the array,
    # return -1 if not present
    return index

def binary_search(array, x):
    
    index = -1 
    
    """
    Insert your code here

    """ 
    sorted_array = sorting_algorithm(array) #sort the array
    
    l, r = 0, len(sorted_array) - 1 #set left pointer to the beginning of the array and the right pointer to the end of it
    
    while l <= r: #while left pointer is smaller or equal the right pointer => middle
        
        mid = (l + r) //2 #compute the middle of the array with the floor division as array can be not even
        
        if sorted_array[mid] == x: #if the value at the middle index is equal to the searched value
            index = mid #index = index at the mid
            break #ends the loop
        elif x < sorted_array[mid]: #if the searched value is smaller than the value at the middle index
            r = mid - 1 #point the right index to the left of cur middle
        else:
            l = mid + 1 #else point the left index to the right of cur middle
    
    
    
    # return the position of x in the array,
    # return -1 if not present
    return index 

class Graph:
    @staticmethod #Static used to imporve the function runtime as there won't be an attempt to instantiate an object and does not access any instance-object data, hence static
    def _exec_time(function, *args, **kwargs): #helper function, that takes the sorting algorithm and computes its execution time
        start_time = time.process_time() #Record the start time
        result = function(*args, **kwargs) #Call the function with the positional and keywords parameters in the function
        exec_time = time.process_time() - start_time #Compute the runtime
        return (result, exec_time) #Return the result of the function and its runtime as a tuple
    
    @staticmethod #Static used to imporve the function runtime as there won't be an attempt to instantiate an object and does not access any instance-object data, hence static
    def graph():
        results_linear = {} #dict to store results of the runs
        results_binary = {} #dict to store results of the runs
        for i in range(1000, 10000, 500): #Loop from 1000 to 10000, with the step of 500
            random_array = np.random.randint(1, 100000, size=i) #for each iteration create a random array
            random_number = np.random.randint(1, 100000) #for each iteration create a number that will be searched in the array
            
            time_binary = Graph._exec_time(binary_search, random_array, random_number)#compute exec time for binary search
            time_linear = Graph._exec_time(linear_search, random_array, random_number)#compute exec time for linear search
            results_linear[i] = time_linear[1] #save the excec time
            results_binary[i] = time_binary[1] #save the excec time


        plt.figure(figsize=(10, 6)) #initialize an empty graph with the width of 10 and height of 6
        plt.plot(list(results_linear.keys()), list(results_linear.values()), label="Linear Search", marker='o') #Plot the curve for the Linear search results, taking keys of the dictionary as the y axis, and values of the dictionary as a x axis, add label and a marker
        plt.plot(list(results_binary.keys()), list(results_binary.values()), label="Binary Search", marker='x') #Plot the curve for the Binary search results, taking keys of the dictionary as the y axis, and values of the dictionary as a x axis, add label and a marker

        plt.xlabel("Array size") #add x axis label
        plt.ylabel("CPU execution time")  #add y axis label
        plt.title("Execution time vs array size") #add graph title
        plt.legend() #add the legend of the graph

        plt.show() #show the graph



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


