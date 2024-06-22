#Binary Search in a 2D array

def search_2d_array(array, target):
    if not array or not array[0]:
        return False
    
    rows = len(array)
    cols = len(array[0])
    
    row, col = 0, cols - 1 
    
    while row < rows and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False

array = [
    [1, 4, 7, 11],
    [2, 3, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 17
print(search_2d_array(array, target))  