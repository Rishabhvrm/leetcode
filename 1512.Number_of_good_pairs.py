from typing import List
def numIdenticalPairs(nums: List[int]) -> int:
    
    ## APPROACH-1: BRUTE FORCE, 2 for loops
    ## T(N): O(N * N)
    ## SPACE: O(1)

    # count, l = 0, len(nums)

    # for i in range(l):
    #     for j in range(i+1, l):
    #         if nums[i] == nums[j]:
    #             count += 1

    # return count

    ## APPROACH-2: count
    ## T(N): O(N * N)
    ## SPACE: O(1)

    # pairs_count = 0
    # for ele in set(nums):
    #     ele_count = nums.count(ele)
    #     pairs_count += (ele_count * (ele_count-1))/2

    # return int(pairs_count)


    ## APPROACH-3: using count/math, and Counter (returns hashmap)
    ## T(N): O(N)
    ## SPACE: O(1)

    # pairs_count = 0

    # # returns a hashmap
    # counter = Counter(nums)     # number -> its count
    # for n, c in counter.items():
    #     pairs_count += (c * (c-1)) // 2

    # return pairs_count


    ## APPROACH-4: keep count by creating a hashmap/dict
    ## T(N): O(N)
    ## SPACE: O(1)

    count = {}          # n -> c
    pair_count = 0

    for ele in nums:
        if ele not in count:
            count[ele] = 1
        
        else:
            # add to pair count as soon as you see a repeatition
            pair_count += count[ele]
            count[ele] += 1
    
    return pair_count

print(numIdenticalPairs(nums=[1,1,1,1]))