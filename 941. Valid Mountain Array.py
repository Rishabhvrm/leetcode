from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1: return False
        
        peak_val = max(arr)
        peak = arr.index(peak_val)
        
        # peak can't be first or last
        if peak == 0 or peak == len(arr) - 1:
            return False

        # before peak, everything should be in strictly increasing order
        for i in range(1, peak + 1):
            # if arr[i] - arr[i - 1] <= 0:        # check if anything is decrementing or equal
            if arr[i - 1] >= arr[i]:
                return False

        # after top, everything should be in strictly decreasing order
        for i in range(peak, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False

        # if everything else is fine then return True
        return True

    '''
    using pointers
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 1: return False

        L = len(arr)
        up, down = 0, L - 1

        while up < L - 1 and arr[up] < arr[up + 1]:
            up += 1
        
        while 1 < down and arr[down - 1] > arr[down]:
            down -= 1

        return up == down and 0 < up and down < len(arr) - 1
