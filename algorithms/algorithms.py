def recursive_binary_search(data, low, high, element):
    if low > high:
        return None
    elif data[(low + high)//2] == element:  # If middle element of array equal to what we are 
        return (low + high)//2              # looking for, return pos of the element
    # If element we are looking for is smaller than middle element of array call func recursivly
    # for left part of array
    elif element < data[(low + high)//2]:
        recursive_binary_search(data, low, (low + high)//2 - 1, element)
    # Else call func for right part of array
    else:
        recursive_binary_search(data, (low + high)//2 + 1, high, element)

def binary_search(data, element):
    low = 0 # Set low to lowest index of array
    high = len(data) - 1 # Same for high
    while low <= high:
        if data[(low + high)//2] == element:
            return (low + high)//2
        elif data[(low + high)//2] > element: # Element we are looking for is on the left 
            high = (low + high)//2 - 1 # Set high to middle index of array
        else:
            low = (low + high)//2 + 1 # Set low to middle index of array
    return None

def selection_sort(array):
    for i in range(0,len(array) - 1):
        mininum = i
        for j in range(i + 1, len(array)): # Searching min element in array from index i+1
            if array[j] < array[mininum]:
                mininum = j
        array[i], array[mininum] = array[mininum], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        j, key = i - 1, array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j] # Go down from key's index. If curr element is bigger than key
            j -= 1                  # move it to it's index+1
        array[j + 1] = key  # If curr element is smaller than key swap them

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right): # Left and right are 2 sorted arrays
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2 # Split array into 2 halves and call func recursivly for each half
        left_partition = merge_sort(array[:mid])
        right_partition = merge_sort(array[mid:])
        return merge(left_partition, right_partition) # merge all parts

def partition(array, low, high):
    pivot = array[high]
    i = low - 1  # Pos of the very right elem of subarray with elements smaller than pivot
    for j in range(low, high):
        if array[j] <= pivot:  # If elem smaller then pivot move border of L subarray
            i = i + 1
            array[i], array[j] = array[j], array[i]  
    array[i + 1], array[high] = array[high], array[i + 1]  # Swap the very left elem of R subarray 
    return i + 1                                           # with the pivot
        
def quick_sort(array, low, high):
    if low < high:
        pivot_pos = partition(array, low, high)  # Get pos of pivot
        quick_sort(array, low, pivot_pos - 1)  # Call func recursivly for lest and right part
        quick_sort(array, pivot_pos + 1, high)

def count_keys_less(array, keys_range):
    equal = [0 for i in range(0, keys_range + 1)]
    less = [0 for i in range(0, keys_range + 1)]
    for i in range(0, len(array)):
        equal[array[i]] += 1
    for i in range(1, keys_range + 1):
        less[i] = less[i - 1] + equal[i - 1]
    return less

def counting_sort(array, less):
    result = [0 for i in range(0, len(array))]
    for i in range(0, len(array)):
        key = array[i]
        result[less[key]] = key
        less[key] += 1
    return result


lst = [1,4,7,9,14,18,34,57,87]
ppt = [1, 4, 3, 3, 6, 4, 5, 1, 1, 2, 0, 2, 2, 3, 3, 1, 2, 5, 5, 4, 4]
lss = [34, 1, 23, 789, 2, 12, 33, 12, 83, 123]
# quick_sort(lss, 0, len(lss) - 1)
# print(lss)
# print(counting_sort(ppt, count_keys_less(ppt, 6)))
