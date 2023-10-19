from typing import List
def canBeEqual(target: List[int], arr: List[int]) -> bool:
    
    ## APPROACH-1: USING SORTING
    ## TIME COMPLEXITY: O(N * LOG N)
    ## SPACE COMPLEXITY: O(1)

    # we can sort both arrays and check if they are equal
    # return sorted(target) == sorted(arr)
    # target.sort()
    # arr.sort()
    # return target == arr


    ## Using Hashmap: count the frequency of elements
    ## TIME COMPLEXITY: O(N)
    ## SPACE COMPLEXITY: O(N)

    hm = {}
    # store frequency in dict
    # ele: its count
    for ele in target:
        hm[ele] = hm.get(ele,0) + 1

    # count frequency in 'arr', decrease ele count in hm
    for ele in arr:
        hm[ele] = hm.get(ele,0) - 1
    
    # check if all counts are zero
    # if not, we can't make arr equal to target
    for k,v in hm.items():
        if v != 0: return False

    # if all counts are zero, return True
    return True
    