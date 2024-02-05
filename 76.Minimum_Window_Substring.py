from collections import Counter
class Solution:

    # correct when target doesn't have duplicates
    # sliding window ~ start a window at each idx and go till end of s
    ## TIME: O( n * n )
    def min_window_brute_force_t_without_duplicates(self, s, t):
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
                min_res, min_len = ele, len(ele)
        return min_res


    # works when target has duplicates
    # sliding window ~ start a window at each idx and go till end of s
    ## TIME: O( n * n ), TLE, 265 / 267 testcases passed
    def min_window_brute_force(self, s, t):
        results = []

        for i in range(len(s)):
            t_count = Counter(t)
            
            for j in range(i, len(s)):
                # skip chars that are not in t for left pointer
                if s[i] not in t_count:
                    break
                
                # if curr char is in t (right pointer), decrement its value
                if s[j] in t_count.keys():
                    t_count[s[j]] = max(0, t_count[s[j]] - 1)   # don't let the key value go to -ve
                    
                # check for every key in t_count if its value is 0
                val_count = 0
                for val in t_count.values():
                    if val == 0:
                        val_count += 1              # count # of keys that has value as 0
                
                # if all keys has their values as 0
                # it means the current string[i:j+1] has all the required values
                # add it to result set
                if val_count == len(t_count):
                    results.append(s[i:j + 1])
                    break
        
        # print(results)
        min_len, res = float('inf'), ""
        for ele in results:
            if len(ele) < min_len:
                min_len, res = len(ele), ele
        return res
    

obj = Solution()

# without duplicates
s, t = "ADOBECODEBANC", "ABC"
# print(obj.min_window_brute_force_t_without_duplicates(s, t))
# print(obj.min_window_brute_force_t_without_duplicates('a', 'a'))

# with duplicates
s, t = "ADOABCAB", "AABC"
# print(obj.min_window_brute_force(s, t))
# print(obj.min_window_brute_force('a', 'aa'))
s, t = "aaaaaaaaaaaabbbbbcdd", "abcdd"
print(obj.min_window_brute_force(s, t))