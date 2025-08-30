def quick_sort(arr):
    #Base case
    if len(arr) <= 1:
        return arr
    

    pivot = arr[0]
    

    left = []    
    right = []   
    

    for i in range(1, len(arr)):  
        current = arr[i]
        if current < pivot:
            left.append(current)      
        else:
            right.append(current)     
    
    #Recursive case
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    

    return sorted_left + [pivot] + sorted_right



unsorted_arr = [3, 7, -6, 10, -2]
sorted_arr = quick_sort(unsorted_arr)
print("Sorted array is:", sorted_arr)