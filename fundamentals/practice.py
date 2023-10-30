## HELPER FOR REVERSE TRAVERSAL EXAMPLE
def find_last_number(nums):
    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] > -1:
            return idx
        
# print(find_last_number([2,1,0,10,-1,-1,-1]))

## 1. REVERSE TRAVERSAL EXAMPLE
## Given an array, replace each even number with twice of the occurance of same number
## do it in-place, input contains space for cloning, empty space denoted by -1
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
print(f'function => reverse([1,2,3,4]) Output => {reverse([1,2,3,4])}')
print('------------------------------------------------')