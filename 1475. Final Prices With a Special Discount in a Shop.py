# monotonically decreasing
def nextGreaterElement(nums):
    stack = []
    result = [-1] * len(nums)  # Default result if no greater element exists
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result


print(nextGreaterElement([10,5,20,3,16]))


class Solution:
    '''
    [10, 20, 5, 16, 2]
    [5, 15, 3, 14, 2]

          i
    8,4,6,2,3
        2,2,3
    4,2,4,2,3
    '''
    from typing import List
    # monotonically increasing
    def finalPrices(self, prices: List[int]) -> List[int]:
        # inc_stack = [(prices[0],0)]
        inc_stack = []
        top = -1

        for i in range(len(prices)):
            while inc_stack and inc_stack[top][0] >= prices[i]:
                price, idx = inc_stack.pop()
                prices[idx] = prices[idx] - prices[i]
            
            inc_stack.append((prices[i], i))            # just idx is enough

        return prices