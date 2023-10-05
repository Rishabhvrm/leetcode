
def findDuplicate(nums) -> int:

    # def binary_search(ele, i):
    #     l = i
    #     r = len(nums) - 1
    #     while l <= r:
    #         mid = (l+r)//2
    #         if nums[mid] == ele:
    #             return True
    #         l += 1
    #         r -= 1

    # for i in range(len(nums)):
    #     if binary_search(nums[i], i):
    #         return nums[i]


    ## APPROACH 2: FLOYD'S FAST AND SLOW POINTERS
    ## T(N): O(N)
    ## SPACE: CONSTANT
    
    slow, fast = 0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

nums = [2,1,2]
nums1 = [1,3,4,2,2]
print(findDuplicate(nums1))

