from typing import List
class Solution:
    '''
                                                 *
    arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    {2: 0, 3:0, 1:0, 4:0, 6:0, 7:1, 9:0, 19:1}

    22222223  2
    2: 5
    3: 1
    
    res = [2,2,2,1,4,3,3,9,6,7,19]

    Approach-1: make a map of val->occ
    add eles in res acc to arr2, use occ from map
    sort map and add remaining values from arr1
    Note: Decrement occ from map after adding to res
    Time: O(n) + O(n * log n)
    Space: O(n), hashmap

    '''
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        val_occ = defaultdict(int)    # val -> occurance
        res = []
        
        # fill hashmap
        for n in arr1:
            val_occ[n] += 1

        # make result using arr2, use occ from hashmap, update hashmap
        for n in arr2:
            for _ in range(val_occ[n]):
                res.append(n)
            val_occ.pop(n)

        # add any remaining values from hashmap, if any
        if val_occ:
            # sort hashmap
            val_occ = dict(sorted(val_occ.items()))

            # add values to res
            for k, v in val_occ.items():
                for _ in range(v):
                    res.append(k)

        return res

    '''
    Approach-2: counting sort, 
    Note: decrement count after adding to res
    Time: O(n)
    Space: O(k), max val in arr1

    arr1 = [2,3,1,3,2,4,6,7,9,2,10], arr2 = [2,1,4,3,9,6]

    0 1 2 3 4 5 6 7 8 9 10
   [  0 0 0 0   0 1   0  1]

   22211433967 10

    '''
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        N = max(arr1)
        occ = [0] * (N + 1)     # idx: order, values: occurance

        # fill up occurance array
        for n in arr1:
            occ[n] += 1

        # add remaining elements in ascending order
        res = []
        for n in arr2:
            res.extend([n] * occ[n])    # or use for loop 
            occ[n] = 0                  # set val to 0 afterwards
        
        # add remaining elements in ascending order
        for idx, n in enumerate(occ):
            res.extend([idx] * n)

        return res


