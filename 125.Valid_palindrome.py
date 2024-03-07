import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lst = []

        # # take alpha-numeric characters into new list
        # for c in s.lower():
        #     if c in string.ascii_lowercase or c in string.digits:
        #         lst.append(c)

        # # make reverse list
        # rlst = lst[::-1]

        # # compare both lists, checks order
        # if (lst == rlst):
        #     return True

        ## APPROACH-2
        # below code line does not pass all test cases (have to replace every special char)
        # a = s.lower().replace(",","").replace(" ","").replace(":", "").replace(".","")
        
        # it's better to check for right condition instead of avoiding wrong ones
        a = "".join(char for char in s if char.isalnum()).lower()
        return a == a[::-1]

    ## REVISIT
    '''
    APPROACH-1: process the str first to remove extra stuff, 
    the, 2 pointers, start and end to check if chars are equal
    TIME: O(N)
    SPACE: O(N), creates new lists
    '''
    def isPalindrome(self, s: str) -> bool:
        processed = []
        for char in s:
            if char.isalnum(): processed.append(char.lower())
        
        left, right = 0, len(processed)-1
        while left < right:
            if processed[left] != processed[right]: return False
            left += 1
            right -= 1
        return True

    '''
    APPROACH-2: process the str first to remove extra stuff, 
    then, 2 pointers, start and end to check if chars are equal
    keep skipping unvalid chars
    TIME: O(N)
    SPACE: O(1)
    '''
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        left, right = L, R

        while left < right:
            # we can use the built-in char.isalnum() as well                            # skip all non-alphanumeric chars from left and right
            while left < right and not self.is_alpha_numeric(s[left]):              
                left += 1
            while left < right and not self.is_alpha_numeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():                                     # check palindrome condition
                return False
            left, right = left + 1, right - 1
        return True

    def is_alpha_numeric(self, c):
        return ((ord("A") <= ord(c) <= ord("Z")) or
                (ord("a") <= ord(c) <= ord("z")) or
                (ord("0") <= ord(c) <= ord("9")))