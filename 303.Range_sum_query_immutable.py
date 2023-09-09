class NumArray:

    ##  BRUTE FORCE, T(N) = O (N * N) 

    # def __init__(self, nums: List[int]):
    #     self.nums = nums
        
    # def sumRange(self, left: int, right: int) -> int:
    #     # initialise sum
    #     sm = 0
        
    #     # traverse from left to right (inclusive)
    #     for i in range(left, right+1):
    #         sm += self.nums[i]
        
    #     return sm

    ## USING DP
    ## STORE THE SUM WHILE INITIALISING
    ## CONSTANT TIME WHILE CALLING sumRange()

    def __init__(self, nums):
        self.prefix = []
        current_sum = 0
        for ele in nums:
            current_sum += ele
            self.prefix.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right] - 0
        return self.prefix[right] -  self.prefix[left-1]
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)