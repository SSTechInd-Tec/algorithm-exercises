#  function definition

def linear_search(arr, target):
    """
    returns the index of the target if found, else returns None
    """

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    
    return None


#  test

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target1 = 5
target2 = 8
target3 = 10
target4 = 15

result1 = linear_search(arr, target1)
result2 = linear_search(arr, target2)
result3 = linear_search(arr, target3)
result4 = linear_search(arr, target4)

print(result1)
print(result2)
print(result3)
print(result4)


