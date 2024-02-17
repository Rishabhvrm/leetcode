# https://leetcode.com/problems/majority-element/description/

from typing import List


def majorityElement(nums) -> int:
    dict = {}
    n = len(nums)

    # traverse array
    for ele in nums:
        # add element in dict if not present
        if ele not in dict:
            dict[ele] = 1
        # increase count if encountered again
        else:
            dict[ele] = dict[ele] + 1
        
        # if count goes more than n//2, return ele
        if dict[ele] > n//2:
            print(dict)
            return ele
    

nums1 = [2,2,1,1,1,2,2]
nums = [3,2,3]
print(majorityElement(nums))


# middle element in sorted array
nums2 = [1,1,1,2,2,2,3,3,3,3,3,3,3]
nums2.sort()
n = len(nums2)
print(len(nums2)/2)
print(nums2[n//2])

def majorityElement2(nums):
    count = {}
    res, max_count = 0, 0

    for n in nums:
        # increase counter for each value in nums
        # count.get(n, 0) -> returns default value of 0 if n is not present
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > max_count else res
        max_count = max(count[n], max_count)
    return res


d = {1:'one', 2:'two', 3:'three'}
print(d.get(4, 4))

print(majorityElement2(nums2))


    ## APPROACH 2: BAYER MOORE'S VOTING ALGORITHM
    ## IDEA: add a vote(count) for every element encountered. Decrease the vote if a   different element encountered. Majority element will beat every other element in terms of its count
    ## T(N): O(N)
    ## SPACE: O(1)
def majorityElement3(nums):
    count = 0               # count for occurances of majority element
    mjrty_ele = 0           # candidate for majortity element 

    for ele in nums:
        # if count == 0 then it's time to update majority element candidate
        if count == 0: mjrty_ele = ele

        # if current ele is same as mjrty_ele then increase count else decrease it
        count += (1 if ele == mjrty_ele else -1)

    return mjrty_ele

print(majorityElement3(nums2))

'''
REVISIT
APPROACH: count occurances using hashmap,
return key where value is > n/2
TIME: O(N)
SPACE: O(N), hashmap
'''
def majorityElement_revisit(nums: List[int]) -> int:
    counter = {}
    for n in nums: counter[n] = counter.get(n, 0) + 1

    for k, v in counter.items():
        if v > len(nums)/2: return k

'''
REVISIT
APPROACH: Bayer Moore's Voting Algorithm
TIME: O(N)
SPACE: O(1)
'''
def majorityElement_revisit_bayer(self, nums: List[int]) -> int:
    count = 0
    candidate = 0 # could be any arbitary value
    for n in nums:
        if count == 0: candidate = n
        count += 1 if n == candidate else -1
        
    return candidate
    
print(majorityElement_revisit([3,3,4]))