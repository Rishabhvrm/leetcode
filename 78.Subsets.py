from typing import List

'''
APPROACH-1: BACKTRACKING at every step of recursion, 
decide to choose or to not choose the current nums[i]
you have 2 choices at every node of the decision tree
TIME: O(N * 2 ^ N)
SPACE: O(N), subset can atmost store N element, ignoring output array powerset
'''
def subsets(nums: List[int]) -> List[List[int]]:

    power_set = []

    def backtrack(idx, subset):
        # base case
        if idx == len(nums):
            # return power_set.append(copy.deepcopy(subset))
            return power_set.append(subset.copy())

        # decision to NOT include nums[i]
        backtrack(idx + 1, subset)

        # decision to include nums[i]
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
        
    backtrack(0, [])
    return power_set

'''
APPROACH-2: (BACKTRACKING) same as approach-1
coded a lil different
TIME: O(N * 2 ^ N)
SPACE: O(N), subset can atmost store N element, ignoring output array powerset
'''
def subsets2(nums: List[int]) -> List[List[int]]:
    power_set, subset = [], []

    def dfs(idx):
        if idx == len(nums):
            power_set.append(subset.copy())
            return

        subset.append(nums[idx])        # include nums[i]
        dfs(idx + 1)

        subset.pop()                    # not include nums[i]
        dfs(idx + 1)

    dfs(0)
    return power_set


'''
APPROACH-3: RECURSION
using base and addon list
at every iteration, expand base and shrink addon
TIME: O(N * 2 ^ N)
SPACE: no extra space, but recursion stack
'''
def subsets3(nums: List[int]) -> List[List[int]]:
    def helper(base: List[int], addon: List[int]) -> None:
        for idx, n in enumerate(addon):
            new_base = base[:] + [n]
            power_set.append(new_base)
            helper(new_base, addon[idx + 1:])

    power_set = []
    power_set.append([])                     # for subset of size 0
    for n in nums: power_set.append([n])     # for subsets of size 1
    
    for idx, n in enumerate(nums):           # for subsets of size 2 or more
        helper([n], nums[idx + 1 : ])
    return power_set



# print(subsets([1,2,3]))
print(subsets2([1,2,3]))