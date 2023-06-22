class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        lst = [ele for ele in str(x)]               # convert to list
        lst_rv = lst[::-1]                          # reverse list

        if lst == lst_rv: return True



# ---------------------------------------------------------------------------

# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# ---------------------------------------------------------------------------
