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


class Graph:
    @staticmethod #Static used to imporve the function runtime as there won't be an attempt to instantiate an object and does not access any instance-object data, hence static
    def _exec_time(function, *args, **kwargs): #helper function, that takes the sorting algorithm and computes its execution time
        start_time = time.process_time() #Record the start time
        result = function(*args, **kwargs) #Call the function with the positional and keywords parameters in the function
        exec_time = time.process_time() - start_time #Compute the runtime
        return (result, exec_time) #Return the result of the function and its runtime as a tuple

    @staticmethod # -||-
    def graph():
        results_bubble = {} #dict to store results of the runs
        results_insertion = {} #dict to store results of the runs
        for i in range(100, 1500, 50): #Loop from 100 to 1500, with the step of 50
            random_array = np.random.randint(1, 100000, size=i) #for each iteration create a random array
        
            time_bubble = Graph._exec_time(bubblesort, random_array) #compute exec time for bubblesort
            time_insertion = Graph._exec_time(insertionsort, random_array)#compute exec time for insertionsort
            results_bubble[i] = time_bubble[1] #save the excec time
            results_insertion[i] = time_insertion[1] #save the excec time

        plt.figure(figsize=(10, 6)) #initialize an empty graph with the width of 10 and height of 6
        plt.plot(list(results_bubble.keys()), list(results_bubble.values()), label="Bubblesort", marker='o') #Plot the curve for the bubblesort results, taking keys of the dictionary as the y axis, and values of the dictionary as a x axis, add label and a marker
        plt.plot(list(results_insertion.keys()), list(results_insertion.values()), label="Insertionsort", marker='x')#Plot the curve for the insertionsort results, taking keys of the dictionary as the y axis, and values of the dictionary as a x axis, add label and a marker

        plt.xlabel("Array size") #add x axis label
        plt.ylabel("CPU execution time") #add y axis label
        plt.title("Execution time vs array size") #add graph title
        plt.legend() #add the legend of the graph

        plt.show() #show the graph

# ----------------------------
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

