import numpy as np 
import time
import matplotlib.pyplot as plt
import pandas as pd 

def sorting_algorithm_graph( ):
    

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 
   

 

   result_insertion = {}
   for i in range(1000, 10000, 1000):
       random_array = np.random.randint( 1, 100, size=i)
       _, exec_time = sorting_algorithm(random_array)
       result_insertion[i] = exec_time
   
   df = pd.DataFrame(result_insertion.values(), index=(x for x in range(1000, 10000, 1000)))


   print(df) 
#    plt.plot(result_insertion.keys(), result_insertion.values())
#    plt.show()


def bubblesort( unsorted_array ):

    n = len( unsorted_array )
    #Create a copy of the unsorted array so to not modify it
    #and modify the sorted_array only
    sorted_array = np.copy(unsorted_array)
    right = False

    while right != True:
        swaps = 0
        for i in range(n-1):
            if sorted_array[i]>sorted_array[i+1]:
                sorted_array[i], sorted_array[i + 1] = sorted_array[i + 1], sorted_array[i]
                swaps += 1

        if swaps == 0:
            right = True

    
    cpu_execution_time = time.process_time()

    return (sorted_array,cpu_execution_time)



def sorting_algorithm( unsorted_array ):
    
   n = len( unsorted_array )
   sorted_array = np.copy( unsorted_array)

   """
   Insert your code here (the bubble or the insertion sorting)

   """ 

   #Insertion sort
   for i in range(1, n):
        j = i - 1
        while j >= 0 and sorted_array[j + 1] < sorted_array[j]:
            tmp = sorted_array[j + 1]
            sorted_array[j + 1] = sorted_array[j]
            sorted_array[j] = tmp
            j -= 1
   cpu_execution_time = time.process_time()
   return (sorted_array, cpu_execution_time)


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


    
if __name__ == "__main__":
    array1 = np.array([1,5,3,2,55,10])
    print(sorting_algorithm(array1))

    array4 = np.array([1,5,3,2,55,10])
    print(bubblesort(array4))

    array2 = np.array([1,2,5,7,8,10,11,12])
    print(binary_search(array2, 7))

    array3 = np.array([1,2,5,7,8,10,11,12])
    print(linear_search(array3, 7))

    sorting_algorithm_graph()

