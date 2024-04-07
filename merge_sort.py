#  functions definitions

def merge_sort(arr):
    """
    Sorts a list in ascending order.
    Returns a new sorted list

    Divide: Find the midpoint if the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n) time.
    """

    if len(arr) <= 1:
        return arr 
    
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(arr):
    """
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right

    Takes overall O(log n) time.
    """

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    return left, right


def merge(left_arr, right_arr):
    """
    Merges two lists (arrarys), sroting them in the process
    Returns a new merged list

    Takes in overall O(n) time.
    """

    l = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            l.append(left_arr[i])
            i += 1
        else:
            l.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        l.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        l.append(right_arr[j])
        j += 1

    return l


#  test

def verify_sorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True 

    return arr[0] < arr[1] and verify_sorted(arr[1:])

arr1 = [1, 4, 7, 5, 8, 9, 2, 12, 54, 34]
arr2 = [1, 4, 7, 5, 8, 9, 2, 12]
arr3 = [5]

result1 = verify_sorted(merge_sort(arr1))
result2 = verify_sorted(merge_sort(arr2))
result3 = verify_sorted(merge_sort(arr3))

print(result1)
print(result2)
print(result3)

