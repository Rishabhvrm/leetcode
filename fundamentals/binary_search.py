## RECURSIVE BINARY SEARCH
def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2

        # target found
        if arr[mid] == target:
            return mid
        # target lies in first half
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, left, mid)
        # target lies in second half
        elif target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return -1   # target not found

arr = [1,3,4,7,9,10,13,14,18,25,30]
target = 3
print(f'''Recursive binary search: 
    arr: {arr} 
    target: {target} 
    target found at arr idx: {binary_search_recursive(arr, target, 0, len(arr) - 1)}''')


print()


## ITERATIVE BINARY SEARCH
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2

        # target found
        if target == arr[mid]: return mid
        # target lies in first half, update right
        elif target < arr[mid]:
            right = mid
        # target lies in second half, update left
        elif target > arr[mid]:
            left = mid
    return -1   # target not found

target = 14
print(f'''Iterative binary search: 
    arr: {arr} 
    target: {target} 
    target found at arr idx: {binary_search_iterative(arr, target)}''')

print()

## USING IN-BUILT BINARY SEARCH FUNCITONS
import bisect

arr_2 = [1, 2, 2, 2, 3, 4, 5, 6]
target_2 = 2

# returns the idx at which target value should be inserted in a sorted sequence
left_idx = bisect.bisect_left(arr_2, target_2)
right_idx = bisect.bisect_right(arr_2, target_2)

print(f'''arr_2: {arr_2}
target_2: {target_2}''')

print(f'left_idx: {left_idx}')
print(f'right_idx: {right_idx}')

if left_idx != right_idx:
    print(f"Target: '{target_2}' found between indices {left_idx} and {right_idx - 1}")
else:
    print(f"Target: '{target_2}' not found in the array")