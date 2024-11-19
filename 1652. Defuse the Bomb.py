from typing import List
class Solution:
    '''
    Approach: Brute force, simulate
    sign of k determines direction
    magnitude of k determines steps to take

    if -ve, reverse the array and reverse the ans
    2,4,9,3
    3,9,4,2
    13,6,5,12
    '''
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)

        if k < 0:
            code = code[::-1]
        
        if k == 0:
            return [0] * l

        res = []

        for i in range(l):
            count = 1
            curr_ele = 0
            while count <= abs(k):
                curr_ele += code[(i + count) % l]
                count += 1
            res.append(curr_ele)

        return res[::-1] if k < 0 else res


    '''
    Same as above just coded differently
    '''
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        for i in range(N):
            if k > 0:
                # forward
                for j in range(i + 1, i + k + 1):
                    res[i] += code[j % N]
            elif k < 0:
                # backward
                for j in range(i - 1, i - abs(k) - 1, -1):
                    res[i] += code[j % N]

        return res

    '''
    sliding window
    T(N): O(N)
    '''
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        l, r = 0, 0
        curr_sum = 0

        while r < N + abs(k):
            curr_sum += code[r % N]
            
            # shrink w if size goes bigger than k
            if r - l + 1 > abs(k):
                curr_sum -= code[l]
                l += 1
            
            # if window size is equal, decide which cell to fill
            if r - l + 1 == abs(k):
                if k > 0:       # forward
                    res[(l - 1) % N] = curr_sum
                elif k < 0:     # backward
                    res[(r + 1) % N] = curr_sum
            
            # expand
            r += 1


        return res

