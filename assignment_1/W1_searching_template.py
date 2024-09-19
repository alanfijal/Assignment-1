#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors: Insert all your names here
Alan Bruno Fijal, Maria Fiamenghi, Marc Farras, Patricia Cerda
"""

import random, time
import matplotlib.pyplot as plt
import numpy as np
import W2_sorting_template


def sorting_algorithm( unsorted_array ):
    
   n = len( unsorted_array )
   sorted_array = np.copy( unsorted_array)

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 
   sorted_array = W2_sorting_template.insertionsort(sorted_array) #perform sorting, using the imported insertionsort from the sorting template
   return sorted_array #return sorted array


def linear_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """

    for i in range(len(array) - 1): #traverse through the array
        if array[i] == x: #if the value at the current index is equal to the searched value
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
    
    return index


def binary_search_recursive(array, x):
    
    index = -1 
    
    """
    Insert your code here

    """ 
    sorted_array = sorted(array) #We sort the array outside of the recursive call, so that runtime won't be artificially inflated by it 

    def recursion(arr, x, l, r): #recursive function expects: an array, value we are looking for, left most index (left pointer), right most index (right pointer)
        if l > r: 
            return -1  #base case, if the left index is bigger than the right index, we break the recursion stating x was not found 
        
        mid = (l + r) // 2 #compute the mid index 

        if arr[mid] == x: #if the x we are looking for is equal to the item at the mid position, we return the middle index 
            return mid 
        elif x < arr[mid]: #if the x we are looking for is smaller than the item at the mid position, we call the recursion with the same parameters, except the right index that is swichted to the middle index - 1
            return recursion(arr, x, l, mid -1)
        else: #if the x we are looking for is greater than the item at the mid position, we call the recursion with the same parameters, except the left index that is swichted to the middle index + 1
            return recursion(arr, x, mid + 1, r)
    
    # return the position of x in the array,
    # return -1 if not present
    index = recursion(sorted_array, x, 0, len(sorted_array) - 1) #call the function with the correct parameters 
    return index 

class Graph:
    def __init__(self, *functions): #user can either pass the functions when instantiating the class, or when calling the function
        self.functions = functions
        
    @staticmethod #Static used to imporve the function runtime as there won't be an attempt to instantiate an object and does not access any instance-object data, hence static
    def _exec_time(function, *args, **kwargs): #helper function, that takes the sorting algorithm and computes its execution time
        start_time = time.perf_counter() #Record the start time, used perf_counter for more precise measurment 
        result = function(*args, **kwargs) #Call the function with the positional and keywords parameters in the function
        exec_time = time.perf_counter() - start_time #Compute the runtime, used perf_counter for more precise measurment 
        return (result, exec_time) #Return the result of the function and its runtime as a tuple
    
    def graph(self, *functions): 
            functions_to_graph = functions if functions else self.functions #if user did not pass any functions when callin the functions, we use the functions passed through instantiation of the class

            if not functions_to_graph:
                raise ValueError("Error, no functions were provided.") #Error raised when functions_to_graph are empty 
            
            results_holder = {f.__name__: {} for f in functions_to_graph} #Dictionary to hold the results, the name of the function: empty dictionary 

            for i in range(1000, 10000, 500): #Loop from 1000 to 10000, with the step of 500
                random_array = np.random.randint(1, 100000, size=i) #for each iteration create a random array
                random_number = np.random.randint(1, 100000) #for each iteration create a number that will be searched in the array

                for f in functions_to_graph: #traverse through the functions to be graphed
                    _, exec_time = self._exec_time(f, random_array, random_number) #compute the runtime using the class function 
                    results_holder[f.__name__][i] = exec_time #store the results in the dictionary corresponding to the name of the function 

            


            plt.figure(figsize=(10, 6)) #initialize an empty graph with the width of 10 and height of 6
            markers = ['x', 'o', '*', 'k', 'p'] #markers avaiable 
            for index, f in enumerate(functions_to_graph): #Grab index and the function while traversing through functions to graph 
                sizes = list(results_holder[f.__name__].keys()) #Get the keys of the results dict, that correspond to the sizes of the arrays 
                times = list(results_holder[f.__name__].values()) #Get the values of the results dict, that correspond to runtimes of the operations  
                plt.plot(sizes, times, label=f.__name__, marker=markers[index]) #plot the graph, using our collected data, label with the current function and marker equivalent to the marker from the list at the current index 

            

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
idx_bs = binary_search_recursive( sorted_array, x )

if idx_bs != -1:
    print("Item", x, "is present at index ", idx_bs)
else:
    print("Element", x, "is not present")



