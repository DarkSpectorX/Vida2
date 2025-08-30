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


def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

arr = quick_sort([1, 3, 5, 8, -1, 5, 15, 6])

result = binarySearch(arr, target=-1)

if result == False:
    print(f"Your index number is : {result}")
    print(f"sorted array is : {arr}")
else:
    print(f"your number wast find...")