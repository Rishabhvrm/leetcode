from collections import Counter
class Solution:

    # correct when target doesn't have duplicates
    def min_window_brute_force_t_without_duplicates(self, s, t):
        ## TIME: O( n * n )
        res = []
    
        for i in range(len(s)):
            target_set = set(t)

            for j in range(i, len(s)):
                if s[j] in target_set:
                    target_set.remove(s[j])
                if not target_set:                  
                    # when all elements of t are found in s, add to result
                    res.append(s[i : j + 1])
                    break
        
        print(res)
        
        min_len, min_res = float("inf"), ""
        # find min length string
        for ele in res:
            if len(ele) < min_len:
                min_res = ele
        return min_res

s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
# print(obj.minWindow(s, t))
print(obj.min_window_brute_force_t_without_duplicates(s, t))
print(obj.min_window_brute_force_t_without_duplicates('a', 'a'))