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
