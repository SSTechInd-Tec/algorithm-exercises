#  function definition

def binary_search(arr, target):
    """
    returns the index of the target if found, else returns None
    """
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2

        if arr[mid_index] == target:
            return mid_index
        
        elif arr[mid_index] < target:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1

    return None

#  test

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target1 = 5
target2 = 8
target3 = 10
target4 = 15

result1 = binary_search(arr, target1)
result2 = binary_search(arr, target2)
result3 = binary_search(arr, target3)
result4 = binary_search(arr, target4)

print(result1)
print(result2)
print(result3)
print(result4)

