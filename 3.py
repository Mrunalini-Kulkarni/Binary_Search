#Binary Search to find the floor and ceil of an element in an array

def find_floor(arr, target):
    left, right = 0, len(arr) - 1
    floor_value = None

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            floor_value = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    return floor_value

def find_ceil(arr, target):
    left, right = 0, len(arr) - 1
    ceil_value = None

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            ceil_value = arr[mid]
            right = mid - 1

    return ceil_value

arr = [4, 5, 8, 6, 10, 14]
target = 9
print(find_floor(arr, target))  
print(find_ceil(arr,target))