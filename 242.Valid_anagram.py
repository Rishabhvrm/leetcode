import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## APPROACH-1: USING SORTING
        ## TIME: O(N * LOG N)
        ## SPACE: O(1)
        return sorted(s) == sorted(t)
        
        ## APPROACH-2: USING COUNTER
        ## TIME: O(N), len(s) + len(t)
        ## SPACE: O(N)
        # return s_count == t_count

        ## APPROACH 3: USING HASHMAP, CREATING COUNTER(above) OURSELVES
        ## TIME: O(N), len(s) + len(t)
        ## SPACE: O(N)
        # if len(s) != len(t): return False

        # # using counter
        # s_count, t_count = {}, {}

        # for i in range(len(s)):
        #     s_count[s[i]] = 1 + s_count.get(s[i], 0)
        #     t_count[t[i]] = 1 + t_count.get(t[i], 0)

        # for k in s_count:
        #     if s_count[k] != t_count.get(k, 0): return False
        # return True

 
