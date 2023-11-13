## HELPER FOR REVERSE TRAVERSAL EXAMPLE
def find_last_number(nums):
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] > -1:
            return idx
        
# print(find_last_number([2,1,0,10,-1,-1,-1]))

## 1. REVERSE TRAVERSAL EXAMPLE
## Given an array, replace each even number 
## with twice of the occurance of same number
## do it in-place, input contains space for cloning,
## empty space denoted by -1
def clone_even_number(nums):
    if not nums: return -1
    
    end = len(nums) 
    idx = find_last_number(nums)

    while (idx >= 0):
        # odd
        if nums[idx] % 2:
            end -= 1
            nums[end] = nums[idx]
        # even
        else:
            end -= 1
            nums[end] = nums[idx]
            end -= 1
            nums[end] = nums[idx]
        
        idx -= 1
    
    return nums
print('------------------------------------------------')
print(f'function => clone_even_number([2,1,0,10,-1,-1,-1]) Output => {clone_even_number([2,1,0,10,-1,-1,-1])}')
print('------------------------------------------------')




## 2. REVERSE ARRAY USING 'TRAVERSING FROM BOTH ENDS'
def reverse(nums):
    left, right = 0, len(nums) - 1
        
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums
print('------------------------------------------------')
print(f'function => reverse([1,2,3,4,5]) Output => {reverse([1,2,3,4,5])}')
print('------------------------------------------------')




## 3. TWO SUM USING 'TRAVERSING FROM BOTH ENDS'
## Return indices of 2 numbers that add up to target, array is sorted
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return (left, right)
        elif sum < target:
            left += 1
        else:
            right -= 1
    return -1
print('------------------------------------------------')
print(f'function => two_sum([1,2,3,5,7], 5) Output => {two_sum([1,2,3,5,7], 5)}')
print('------------------------------------------------')

        


## 4. PARTITIONING ARRAYS
## 4.1, 4.2 Move all zeros to the start/end of array
def move_zero(nums):
    # if cloud starts from beginning => COLLECT 0'S AT BEGINNING
    # boundary = 0
    # for idx in range(len(nums)):
    #     if nums[idx] == 0:
    #         nums[idx], nums[boundary] = nums[boundary], nums[idx]
    #         boundary += 1

    # if cloud starts from the end => COLLECT 0'S AT END
    boundary = len(nums) - 1
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] == 0:
            nums[idx], nums[boundary] = nums[boundary], nums[idx]
            boundary -= 1

    return nums
print('------------------------------------------------')
print(f'function => move_zero([2,0,1,0,3,3,0]) Output => {move_zero([2,0,1,0,3,3,0])}')
print('------------------------------------------------')


## 4.3 DUTCH NATIONAL FLAG PROBLEM
## Given a pivot, divide an array into 3 secitons. [< pivot | = pivot | > pivot]

def partition_array(nums, pivot):
    start_boundary, end_boundary = 0, len(nums) - 1

    # front partition
    for idx in range(len(nums)):
        if nums[idx] < pivot:
            # swap
            nums[idx], nums[start_boundary] = nums[start_boundary], nums[idx]
            start_boundary += 1

    # end partition
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] > pivot:
            # swap
            nums[idx], nums[end_boundary] = nums[end_boundary], nums[idx]
            end_boundary -= 1

    return nums
print('------------------------------------------------')
print(f'function => partition_array([1,4,5,4,4,6,2,3], 4) Output => {partition_array([1,4,5,4,4,6,2,3], 4)}')
print(f'function => partition_array([3,2,4,1,6,3,7,5], 4) Output => {partition_array([3,2,4,1,6,3,7,5], 4)}')
print('------------------------------------------------')
    

## 5. KADANE'S ALGORITHM
## Leetcode 53
## A) Given an integer array nums, 
# find the subarray with the largest sum, 
# and return its sum.
## 1. BRUTE FORCE - T(N): O(N * N)

def max_sum_subarray(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    
    return max_sum
print('------------------------------------------------')
print(f'function => max_sum_subarray([4,-1,2,-7,3,4]) Output => {max_sum_subarray([4,-1,2,-7,3,4])}')
print(f'function => max_sum_subarray([-2,-3,4,-1,-2,1,5,-1]) Output => {max_sum_subarray([-2,-3,4,-1,-2,1,5,-1])}')
print('------------------------------------------------')

## 2. KADANE'S: O(n)
def max_sum_subarray_kadens(nums):
    max_sum = nums[0]
    curr_sum = 0

    for n in nums:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(curr_sum, max_sum)

    return max_sum
print('------------------------------------------------')
print(f'function => max_sum_subarray_kadens([4,-1,2,-7,3,4]) Output => {max_sum_subarray_kadens([4,-1,2,-7,3,4])}')
print(f'function => max_sum_subarray_kadens([-2,-3,4,-1,-2,1,5,-1]) Output => {max_sum_subarray_kadens([-2,-3,4,-1,-2,1,5,-1])}')
print('------------------------------------------------')


## B) SLIDING WINDOW VARIATION OF KADEN'S: O(n)
## Return the left and right index of max subarray sum window, 
## assuming there's only one solution, (not ties)
def sliding_window_kadens(nums):
    max_sum = nums[0]
    curr_sum = 0
    maxL, maxR = 0, 0
    L = 0
    
    for R in range(len(nums)):
        if curr_sum < 0:            # reset curr_sum
            curr_sum = 0
            L = R

        curr_sum += nums[R]
        
        if curr_sum > max_sum:      # update max sum
            max_sum = curr_sum
            maxL, maxR = L, R
            
    return [maxL, maxR]

print('------------------------------------------------')
print(f'function => sliding_window_kadens([4,-1,2,-7,3,4]) Output => {sliding_window_kadens([4,-1,2,-7,3,4])}')
print(f'function => sliding_window_kadens([-2,-3,4,-1,-2,1,5,-1]) Output => {sliding_window_kadens([-2,-3,4,-1,-2,1,5,-1])}')
print('------------------------------------------------')




## 6. SLIDING WINDOW
## SUBARRAY SLIDING WINDOW
## Find a subarray that sums to a target, all +ve int, return indexes

## the reason that we're not moving the right inwards if sum > target is 
## that we know that target can't be achived using the numbers inside the window right now
## because we already calculated the sum for that,
## therefore move the left pointer (some confusion in expanation)
def find_sum_subarray(nums, target):
    left, right = 0,0

    while left < len(nums) and right < len(nums):
        curr_sum = 0
        curr_sum = sum(nums[left : right + 1])

        if curr_sum == target:
            return (left, right)
        elif curr_sum < target:                         # expand window
            right += 1
        elif curr_sum > target:                         # shrink window
            left += 1

    return None

print('------------------------------------------------')
print(f'function => find_sum_subarray([5,3,1,7,6,4,3,2], 14) Output => {find_sum_subarray([5,3,1,7,6,4,3,2], 14)}')
print(f'function => find_sum_subarray([3,1,7,6,24,3,2], 5) Output => {find_sum_subarray([3,1,7,6,24,3,2], 5)}')
print(f'function => find_sum_subarray([3,1,7,6,24,3,2], 5) Output => {find_sum_subarray([3,1,7,6,24,3,2], -1)}')
print('------------------------------------------------')




## 7. SUBARRAY PREFIX SUM
## Find a subarray that sums to 0 (can contain +ve and -ve int), return the indexes
## Sol: Store prefix sum

def prefix_sum_subarray(nums):
    curr_sum = 0
    idx_sum = {}        # sum till idx -> idx

    for idx in range(len(nums)):
        curr_sum += nums[idx]
        # A. First condition of sum being 0
        if curr_sum == 0: return (0, idx)

        # B. Another condition of sum being 0
        # if any new sum == any old sum, 
        # elements btw these two would sum to 0
        if curr_sum in idx_sum:
            return (idx_sum[curr_sum] + 1, idx)
        else: 
            idx_sum[curr_sum] = idx

    return None
print('------------------------------------------------')
print(f'function => prefix_sum_subarray([-1,2,1,-4,2,3,-1,2]) Output => {prefix_sum_subarray([-1,2,1,-4,2,3,-1,2])}')
print(f'function => prefix_sum_subarray([-1,3,1,-4,2,3,-1,2]) Output => {prefix_sum_subarray([-1,3,1,-4,2,3,-1,2])}')
print('------------------------------------------------')




# 2 POINTER SORTING, doesn't work LOL
a = [4,3,1,2,5,15,11]
out = [0] * len(a)
left, right = 0, len(a) - 1
l = len(a)
for i in range(l-1, -1, -1):
    if a[left] > a[right]:
        out[i] = a[left]
        left += 1
    else:
        out[i] = a[right]
        right -= 1
print(out)


## USING REVERSE
print(a.reverse())