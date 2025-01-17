from typing import List

class Solution:
    '''
O   0 1 0
    1 0 1
D   1 1 0


O   0 1
D   1 0

O   0 1
O   1 0 
D   1 1

O   0   or 1
D   1   incorrect
D   0   correct

O   1 1 0 1 1
D   0 1 1 0 0

    '''
    # def doesValidArrayExist(self, derived: List[int]) -> bool:
    #     first, last = 0, 0

    #     for n in derived:
    #         if n == 1:
    #             last = ~last
            
    #     return first == last

    # def doesValidArrayExist(self, derived: List[int]) -> bool:
    #     res = 0
    #     for ele in derived:
    #         res ^= ele
        
    #     return not res

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0