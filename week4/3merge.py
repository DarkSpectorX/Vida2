def merge_sort(arr):
    #Base case
    if len(arr) <= 1:
        return arr

    #Divide it to two array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    #Recursive divide
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    #Merge two array
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []        
    i = j = 0          

    # مقایسه عناصر دو لیست و اضافه کردن کوچکتر
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # اضافه کردن بقیه عناصر (اگر تو یکی از لیست‌ها چیزی مونده باشه)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# تست کد
unsorted_arr = [3, 7, -6, 10, 15, -2, 18, 55]
sorted_arr = merge_sort(unsorted_arr)
print("Sorted array is:", sorted_arr)