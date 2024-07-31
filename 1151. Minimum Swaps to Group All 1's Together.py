'''
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
 

Constraints:

1 <= data.length <= 105
data[i] is either 0 or 1.
'''
from typing import List

class Solution:
    '''
    [1] [1,1]  => 0
    [0], [0,0] => 0
  
    [0,0,0,0,0,1,1,1,1,1,1]
    3

    0 1 2 3 4 5 6 7 8 9 
    0,0,0,0,0,0,0,0,1,1,1,1,1,1
                *                          
    0 1 2 0 1 2 0 1 2 0 1 0 1 0

           *
    010010 1 010000001
                 -----

    00001 = 5 - 1 = 4
    00000 = 5 - 0 = 5
    10 1 01 = 5 - 3 = 2

    ones = 5
    
    number of swaps = ones - # of 1's in curr array 

    11101
    ----
     ----

    4 - 3 = 1
    4 - 3 = 1

    101010
       ---
    3 - 2 = 1
    3 - 1 = 2

    001001
        --

    total = 3


    '''



    '''
    
    0 1 2 3 4 5 6 7 8 9 10
            L           R
    1,0,1,0,1,0,0,1,1,0,1
    
    0 1 2 3 4
    
     L  
    0,0,0,1,0
      R
    z = 2
     
    Approach: Sliding-Window
    # of zeros in the subarray of size total_ones = # of swaps
    Time: O(n)
    Space: O(1)
    '''
    # def minSwaps(self, data: List[int]) -> int:
    #     total_ones = sum(data)
    #     N = len(data)
        
    #     l, r = 0, 0
        
    #     num_of_zeros = 0
        
    #     while r <= total_ones - 1:
    #         if data[r] == 0:
    #             num_of_zeros += 1
    #         r += 1
        
    #     num_of_swaps = min(float('inf'), num_of_zeros)
        
    #     while r < N:
    #         if data[r] == 0:
    #             num_of_zeros += 1
            
            
    #         if data[l] == 0:
    #             num_of_zeros -= 1
                
    #         num_of_swaps = min(num_of_swaps, num_of_zeros)
    #         l, r = l + 1, r + 1
            
    #     return num_of_swaps
    
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)
        zeros = 0               # minimize
        swaps = float('inf')
        
        l = r = 0
        while r < total_ones:
            zeros += 1 if data[r] == 0 else 0
            r += 1
        
        swaps = zeros
            
        while r < len(data):
            zeros += -1 if data[l] == 0 else 0
            zeros += 1 if data[r] == 0 else 0
            
            swaps = min(swaps, zeros)
            l += 1
            r += 1
        
        return swaps