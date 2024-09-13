from typing import List
class Solution:
    '''
    Approach: Brute Force
    Time: O(q * n), for each query, you could traverse the whole array
    Space: O(1)
    TLE 41/42
    '''
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for q in queries:
            l, r = q
            xor_sum = 0
            for i in range(l, r + 1):
                xor_sum ^= arr[i]
            res.append(xor_sum)
        
        return res

    '''
    Approach: Prefix Sum
    Time: O()
    Space: O(1)
    '''
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] ^ n)

        res = []
        for l, r in queries:
            res.append(prefix[r + 1] ^ prefix[l])

        return res
    
    '''
    Approach: Prefix Sum, w/ modifying input
    Time: O(q + n)
    Space: O(1)
    '''
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        res = []
        for l, r in queries:
            total = arr[r]
            remove = 0 if l == 0 else arr[l - 1]
            res.append(total ^ remove)

        return res