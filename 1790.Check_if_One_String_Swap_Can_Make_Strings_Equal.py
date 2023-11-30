class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ## APPROACH: 2 pointers, 
        ## traverse both string and check if curr_val is same in both strings
        ## if yes, move to next
        ## if no, check if curr_val in 2nd str exits in 1st, allow 2 such cases only

        i, j, swap_count = 0, 0, 0
        while i < len(s1):
            if s1[i] != s2[j]:
                if s2[j] in s1:
                    swap_count += 1

            i += 1
            j += 1

        return swap_count == 2
    

obj = Solution()
s1 = "bank"
s2 = "kanb"

s1 = "attack"
s2 = "defend"
print(obj.areAlmostEqual(s1,s2))