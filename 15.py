#Find Rotation Count in Sorted Array

def countRotations(array, n): 
    min = array[0] 
    min_index = 0
    for i in range(0, n): 
      
        if (min > array[i]): 
          
            min = array[i] 
            min_index = i 
          
    return min_index; 

array = [15, 18, 2, 3, 6, 12] 
n = len(array) 
print(countRotations(array, n)) 