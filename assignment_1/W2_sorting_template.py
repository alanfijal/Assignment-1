#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Insert all your names here
Alan Bruno Fijal, Maria Fiamenghi, Marc Farras, Patricia Cerda
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
    right = False #indicates if the array is sorted
    
    while not right: #iterates until no swaps have been made
        swaps= 0 #counter
        for i in range(n-1): #traverse through the array
            if sorted_array[i]>sorted_array[i+1]:  #if the cur element is greater than next
                sorted_array[i], sorted_array[i+1] = sorted_array[i+1], sorted_array[i] #swap them
                swaps += 1 #increase the counter of swaps
                
        if swaps == 0: #indication that no swaps have been made, hence the array is sorted
            right = True #breaks the loop


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
    for i in range(1, n): #traverse through they array starting at the 2nd element
        j = i - 1 #set trailing pointer
        while j >= 0 and sorted_array[j + 1] < sorted_array[j]: #Continue while the trailing pointer exists and cur element is smaller than the element before
            tmp = sorted_array[j + 1] #store the cur element in the temporary variable
            sorted_array[j + 1] = sorted_array[j] #shift cur to the right
            sorted_array[j] = tmp #smaller element allocated into the position emptied by the moved element
            j -= 1 #move the pointer to the left if 0 breaks the loop
    
    
    #Return the sorted array
    return sorted_array



# Function to find the partition position in quicksort
def quicksort_partition(array, left, right):
 
    """
    Insert your code here

    """ 

    pivot = array[right] #Pivot is choosen to the rightmost index
    i = left - 1 #Pointer set to track the smaller element

    for j in range(left, right): #Iterate through the elements and redistribute them around the pivot
        if array[j] <= pivot: #If the current item is smaller or equal to pivot
            i += 1 #Trailing index moved to right
            array[i], array[j] = array[j], array[i] #Swap elements
        
    array[i + 1], array[right] = array[right], array[i + 1] #Swap the element at the pivot index with the element right to the trailing pointer 
    
    return i + 1 #return the partition index 

    


 
# Function to perform quicksort 
def quicksort(array, dummy=0, dummy_node=0): #dummy parameters set for the same reason as mentioned below 

    """
    Insert your code here

    """ 
    def recursion(array, left, right): #sort of a helper function, designed so that the quicksort will be compatible if the function used to create graphs 
        
        if left < right: #as long as left index is smaller than the right, we stay in the recursion 
            partition_index = quicksort_partition(array, left, right) #Set the partition index
            recursion(array, left, partition_index - 1) #Quicksort_Recursion on the left side
            recursion(array, partition_index + 1, right ) #Quicksort_Recursion on the right side 
    
    recursion(array, 0, len(array) - 1) #call the function 
    return array #return sorted_array 
    

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
               

                for f in functions_to_graph: #traverse through the functions to be graphed
                    _, exec_time = self._exec_time(f, random_array) #compute the runtime using the class function 
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

#Generate 10 random numbers between 1 and 10000
random_array = np.random.randint( 1, 10000, size=10)
size = len( random_array )

#Ordering from smallest to largest using Bubble sort
bubble_array = bubblesort( random_array )

#Ordering from smallest to largest using Insertion sort
insertion_array = insertionsort( random_array )

#Ordering from smallest to largest using Quick sort
quick_array = np.copy( random_array)
quicksort( quick_array, 0, len(quick_array) - 1 )

# Print the results
print( "\n Unsorted array of", size, "elements is:\t\t", random_array )
print( "\n Bubble sorted array of", size, "elements:\t\t", bubble_array )
print( "\n Insertion sorted array of", size, "elements:\t", insertion_array )
print( "\n Quick sorted array of", size, "elements:\t", quick_array )
