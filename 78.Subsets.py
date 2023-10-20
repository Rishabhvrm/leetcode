from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    power_set = []

    def backtrack(idx, subset):
        # base case
        if idx == len(nums):
            # return power_set.append(copy.deepcopy(subset))
            return power_set.append(subset.copy())

        # decision to NOT include nums[i]
        backtrack(idx + 1, subset)

        # decision to NOT include nums[i]
        subset.append(nums[idx])
        backtrack(idx + 1, subset)
        # pop the above appended element
        # so it doesn't stay in list for the next round of recursion
        # elements should be added to a fresh list
        # backtrack by removing the last element
        subset.pop()

        # this didn't work because the second argument doesn't return any value
        # it returns None, that's why it tooke me an hour to figure out why it wasn't working
        # backtrack(idx + 1, subset.append(nums[idx]))
        
    # subset = []
    backtrack(0, [])
    return power_set

print(subsets([1,2,3]))