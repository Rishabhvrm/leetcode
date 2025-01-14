from typing import List
class Solution:
    '''
    1 2 3
    3 2 1

          #
    1 3 2 4 5
    2 4 5 3 1
    0 0 1 3 5

A   1 3 2 4
B   2 4 5 3

    c = 3
    0 0 1 3

    Brute force:
    if A[i] == B[j] -> count += 1
    else:
        compare the whole map and only increment count for what's common

    Single Pass:
        use hash-set and as you iterate, keep adding to set
        for each new ele check if it's present in the other set, inc count if it is
        Time:  O(n)
        Space: O(n)
    '''
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        count = 0
        set_a, set_b = set(), set()

        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
            
            if A[i] in set_b:
                count += 1
            
            if B[i] in set_a:
                count += 1
            
            set_a.add(A[i])
            set_b.add(B[i])
            
            res.append(count)

        return res


'''
      #
    1,3,2,4
    3,1,2,4

A   1 3
B   3 1
c = 2
0 2
'''