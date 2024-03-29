from collections import Counter
class Solution:
    ''' SOLUTION-1 '''
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



    ''' SOLUTION-2 '''
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



    ''' SOLUTION-3 '''
    # works when target has duplicates
    # similar to above but cleaner and modular code
    ## TIME: O( n * n ), TLE, 265 / 267 testcases passed
    def min_window_brute_force_2(self, s: str, t: str):
        
        # checks if given window is valid or not
        def check_valid_window(strng) -> bool:      # update this to just start, end
            t_count = Counter(t)
            # if ele occurs in t_count, decrement its value
            for ele in strng:
                if ele in t_count:
                    t_count[ele] = max(0, t_count[ele] - 1)
            
            # a) count 0s in t_count
            val_count = 0
            for v in t_count.values():
                if v == 0:
                    val_count += 1

            # b) check if every key in t_count has 0 value
            return val_count == len(t_count) 

        start, end = 0, 0
        min_str, min_len = "", float('inf')
        # res = []

        # check if the curr_window is valid?
            # if yes: add curr_window to result and move the start pointer (shrink from left)
            # if no: move the end pointer in hope of making it valid (expand from right)

        while end <= len(s):
            while check_valid_window(s[start: end + 1]):            # update this to just start, end
                # don't need this actually
                # res.append(s[start: end + 1])
                curr_min =  s[start: end + 1]  
                if len(curr_min) < min_len:
                    min_str, min_len = curr_min, len(curr_min)      # pick min len str
                start += 1
            else:
                end += 1
       
        # print(res)
        return min_str



    ''' SOLUTION-4 : Optimized'''
    ## TIME: O( n + k ), n = len(s), k = len(t)
    ## SPACE: O( n + k )
    def minWindow(self, s: str, t: str):
        if not s or not t: return ""
        
        t_count = Counter(t)                     # count of unique chars in t
        # need: unique chars in t, that should be present in curr window for it to be valid
        need = len(t_count)

        window_count = {}                        # count of every unique char in curr window
        # need's counterpart for curr window, if have == need, window is valid
        have = 0                                 
        
        left, right = 0, 0

        # tuple: (min_window_length, min_left, min_right)
        ans = float("inf"), None, None

        while right < len(s):
            curr_char = s[right]
            window_count[curr_char] = window_count.get(curr_char, 0) + 1

            if curr_char in t_count and window_count[curr_char] == t_count[curr_char]:
                have += 1

            # keep shrinking window if it's valid
            while left <= right and have == need:
                curr_char = s[left]                         # update curr_char

                if right - left + 1 < ans[0]:               # save smallest window until now
                    ans = (right - left + 1, left, right) 
                
                window_count[curr_char] -= 1                # since left is moving, decrease curr_char's count
                
                # if moving left will make window unvalid, decrease 'have'
                if curr_char in t_count and window_count[curr_char] < t_count[curr_char]:
                    have -= 1

                left += 1                                   # move left => shrink

            right += 1                                      # move right => expand
        
        min_window_len, min_left, min_right = ans
        return "" if min_window_len == float("inf") else s[min_left : min_right + 1]


obj = Solution()

### brute force without duplicates
# s, t = "ADOBECODEBANC", "ABC"
# print(obj.min_window_brute_force_t_without_duplicates(s, t))
# print(obj.min_window_brute_force_t_without_duplicates('a', 'a'))

### brute force with duplicates
# s, t = "ADOABCAB", "AABC"
# print(obj.min_window_brute_force(s, t))
# print(obj.min_window_brute_force('a', 'aa'))
# s, t = "aaaaaaaaaaaabbbbbcdd", "abcdd"
# print(obj.min_window_brute_force(s, t))

### brute force with duplicates modular
s, t = "ADOBECODEBANC", "ABC"
s, t = "ADOABCAB", "AABC"
print(obj.min_window_brute_force_2(s, t))
