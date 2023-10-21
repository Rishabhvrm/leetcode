from typing import List
def subsetsWithDup(nums: List[int]):
    
    def backtrack(idx, subset):
        if idx == len(nums):
            # do not add duplicates
            if subset not in power_set:
                power_set.append(subset.copy()) # or use subset[::]
            return

        # choose to include nums[i]
        subset.append(nums[idx])
        backtrack(idx + 1, subset)
        subset.pop()

        # # another approach to skip duplicates if above one not used
        # while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
        #     idx += 1
        # choose NOT to include nums[i]
        backtrack(idx + 1, subset)

    power_set = []
    subset = []
    # sort input array - to skip the same repeated number
    nums.sort()
    backtrack(0, subset)

    return power_set
    


num = [1,2,2]
print(subsetsWithDup(num))
