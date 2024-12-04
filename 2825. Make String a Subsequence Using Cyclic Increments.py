class Solution:
    '''
    approach: 2 pointers
    check if str2[j] == str1[i] or str1[i] + 1      # take care of z -> a
        if yes, move j
    keep on moving i
    if j reaches the end, return true
    return false 

    '''
    '''
     i
    zc

     j
    ad

    a
    bb      => False

    time: O(n), n: len(str1)
    space: O(1)
    '''
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False

        i, j = 0, 0

        while i < len(str1):
            
            curr = ord(str1[i])

            if (ord(str2[j]) == curr or                     # equal 
                ord(str2[j]) == curr + 1 or                 # equal after one operation
                ord(str2[j]) == curr - 25):                 # z -> a
                # str2[j] == "a" and str1[i] == "z"):       # z -> a
                j += 1
            
            if j == len(str2):
                return True

            i += 1

        return False