#  function definition

def recursive_binary_search(arr, target):
    """
    returns the index of the target if found, else returns None
    """
    if len(arr) == 0:
        return False
    else:
        mid_index = len(arr) // 2
        if arr[mid_index] == target:
            return True
        elif arr[mid_index] < target:
            return recursive_binary_search(arr[mid_index+1:], target)
        else:
            return recursive_binary_search(arr[:mid_index], target)


#  test

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target1 = 5
target2 = 8
target3 = 10
target4 = 15

result1 = recursive_binary_search(arr, target1)
result2 = recursive_binary_search(arr, target2)
result3 = recursive_binary_search(arr, target3)
result4 = recursive_binary_search(arr, target4)

print(result1)
print(result2)
print(result3)
print(result4)

