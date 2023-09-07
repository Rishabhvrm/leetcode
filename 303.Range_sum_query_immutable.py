
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        # initialise sum
        sm = 0
        
        # traverse from left to right (inclusive)
        for i in range(left, right+1):
            sm += self.nums[i]
        
        return sm


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)