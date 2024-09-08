import time
import numpy as np


def binary_search(array, x):
    
 
    index = -1 
    
    """
    Insert your code here

    """ 
    
    l, r = 0, len(array) - 1
    
    while l != r:
        
        mid = (l + r) //2
        
        if array[mid] == x:
            index = mid
            break
        elif x < array[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    if array[l] == x:
        index = l
    
  
    # return the position of x in the array,
    # return -1 if not present
    return index

def linear_search( array, x ):
    
    index = -1 
    
    """
    Insert your code here

    """
    start_time = time.process_time()
    for i in range(len(array) - 1):
        if array[i] == x:
            index = i
    
    
    
    # return the position of x in the array,
    # return -1 if not present
    return index


class Graph:
    def _exec_time(function, *args, **kwargs):
        start_time = time.process_time()
        result = function(*args, **kwargs)
        exec_time = time.process_time() - start_time
        return (result, exec_time)

    def graph():
        result_linear = {}
        results_binary = {}
        
    
    
        


if __name__ == "__main__":
    array1 = np.array([1,1000,2,55,4432,55,69,22])
    print(binary_search(array1, 69))