
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # slow will point to zeros
    # fast will find non-zeros
    # swap nums[slow] with nums[fast]
    slow, fast = 0, 0

    # till fast reaches end
    for fast in range(len(nums)):
        # if fast reaches non-zero => swap 
        # increase both pointers (slow in this loop, and fast is getting increased outside the loop in every iteration)
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        
        



nums = [0,1,2,3]
moveZeroes(nums)