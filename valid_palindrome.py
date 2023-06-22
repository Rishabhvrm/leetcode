import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []

        # take alpha-numeric characters into new list
        for c in s.lower():
            if c in string.ascii_lowercase or c in string.digits:
                lst.append(c)

        # make reverse list
        rlst = lst[::-1]

        # compare both lists, checks order
        if (lst == rlst):
            return True