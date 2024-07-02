from typing import Counter, List


class Solution:
    '''
    Brute-Force: sort and 2 pointers
    Time: O(N * log N)
    Space: O(1)
    '''
    '''
            a
    1 1 2 2 
    2 2
        b
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()

        a, b = 0, 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                a += 1
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                res.append(nums1[a])
                a, b = a + 1, b + 1
        
        return res

    '''
    Using 2 hashmaps for occurance count
    Time: O(N)
    Space: O(N)
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        for k, v in count1.items():
            if k in count2:
                temp = min(v, count2[k])
                for _ in range(temp):
                    res.append(k)
        
        return res

    '''
    using one hashmap
    '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        freq = Counter(nums1)
        
        for n in nums2:
            if n in freq and freq[n] > 0:
                res.append(n)
                freq[n] -= 1

        return res