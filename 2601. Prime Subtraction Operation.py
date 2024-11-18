from typing import List
import math

class Solution:
    '''
    2 3 5 7 11 13
                  # 
    [7,3,4,5] => [2,3,4,5] => True
    [3,4,5,7] => already sorted => True


    [2,4,6,10]

     3 5 2   => can't pick 5
    [5,8,3]
     2,3,1
     
     3. 5   2
     5, 8   3
     2  3.  1

    11 9
    12,12
    1,3
    '''
    '''
    be greedy: subtract as much as you can from the current # so that res is sorted
    '''
    def primeSubOperation(self, nums: List[int]) -> bool:

        def _is_prime(num):
            for i in range(2, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        def _biggest_prime_less_than(num):
            num -= 1        # can only take prime # less than curr_num
            while num >= 2:
                if _is_prime(num):
                    return num
                num -= 1
            return 0        # if num <= 2, don't subtract anything


        arr = nums
        # loop starts from 1, do 0idx here
        arr[0] -= _biggest_prime_less_than(arr[0])

        for i in range(1, len(nums)):
            # arr[i] should be as smallest as possible (Greedy)
            # and greater than arr[i - 1] 
            # => that's why find the biggest prime less that a[i] - a[i - 1]
            arr[i] -= _biggest_prime_less_than(arr[i] - arr[i - 1])
            if arr[i] <= arr[i - 1]:    # should be strictly increasing
                return False

        return True
    
    
'''
Take 2
'''
def primeSubOperation(nums: List[int]) -> bool:
    
    def _is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
            
    
    def _largest_prime_smaller_than(num):
        # pick a prime strictly less than curr num
        num -= 1
        while num >= 2:
            if _is_prime(num):
                return num
            num -= 1
        
        return 0        # if num < 2, subtract 0
    
    nums[0] -= _largest_prime_smaller_than(nums[0])
    
    for i in range(1, len(nums)):
        nums[i] -= _largest_prime_smaller_than(nums[i] - nums[i - 1])
        if nums[i] <= nums[i - 1]:
            return False
    
    return True