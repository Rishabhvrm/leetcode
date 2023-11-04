class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ## APPROACH: Sliding Window
        ## TIME: O(n), traversing through array
        ## SPACE: O(n), set used to check duplicates

        char_set = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            # if found duplicate char, 
            # remove everything from set
            # make window size 0 by keep incrementing left pointer
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])

            curr_len = len(s[l : r + 1])
            max_len = max(max_len, curr_len)

        return max_len
    
s = "abcabcbb"
s = "pwwkew"
s = "acddddxyzwrst"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))