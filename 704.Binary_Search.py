

    
# recursive
'''
def search(self, nums: List[int], target: int) -> int:
    if target not in nums:
        return -1

    l = len(nums)

    # recursive solution
    # if len is even
    if l % 2 == 0:
        # target is in first half
        if nums[l//2 - 1] > target:                 
            return self.search(nums[:l//2], target)

        # target is in second half
        else:                                       
            return l//2 + self.search(nums[l//2:], target)

    # if len is odd
    else:
        # middle element is target
        if nums[l//2] == target:
            return l//2
        
        # target is in first half
        if nums[l//2] > target:                     
            return self.search(nums[:l//2], target)
        
        # target is in second half    
        else:                                       
            return l//2 + self.search(nums[l//2:], target)
'''

def search(nums, target) -> int:
    # two pointers
    l = 0
    r = len(nums) - 1

    while l<=r:
        mid = (l+r)//2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1 
        elif nums[mid] < target:
            l = mid + 1

    return -1

l1 = [-1,0,3,5,9,12]
print(search(l1, 5))