from typing import List
from collections import deque

''''
BRUTE FORCE
T(N): O(N LOG N)
'''
def sortedSquares(nums):
    r = []
    for n in nums:
        r.append(n*n)
    return sorted(r)


'''
Approach: 2 pointers, fill from end
Time: O(n)
Space: O(1)
'''
def sortedSquares(nums):
    l = len(nums)
    out = [0] * l                               # initialize output array
    left, right = 0, l - 1                      # initialize left and right pointers
    
    # range(start:stop:step)
    # start from end, go till start, with step of -1
    # so that output array is sorted
    for i in range(l-1, -1, -1):         

        left_square = nums[left] ** 2           # calculate left and right squares
        right_square = nums[right] ** 2

        if left_square <= right_square:         # compare, assign o/p and move pointers
            out[i] = right_square
            right -= 1
        else:
            out[i] = left_square
            left += 1

    return out

'''
Approach: merge 2 sorted arrays, use deque to make those arrays
Time: O(n)
Space: O(n)

[-4,-1,0,3,10]
ps = [1, 16]
ns = [0, 9, 100]
'''
def sortedSquares(self, nums: List[int]) -> List[int]:
    res, pos_sq, neg_sq = [], deque(), deque()

    # make 2 sorted lists (deques) of squares
    for n in nums:
        if n >= 0:
            pos_sq.append(n ** 2)
        else:
            neg_sq.appendleft(n ** 2)

    # merge
    while pos_sq and neg_sq:
        a = pos_sq[0]
        b = neg_sq[0]

        if a < b:
            res.append(a)
            pos_sq.popleft()
        else:
            res.append(b)
            neg_sq.popleft()

    while pos_sq:
        res.append(pos_sq.popleft())
        
    while neg_sq:
        res.append(neg_sq.popleft())
        
    return res

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))

