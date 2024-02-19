'''
APPROACH: Sliding Window
if incoming char already present in set, 
keep removing chars from set that s[l] points 
till occurace of incoming duplicate char is also removed
make window shrink by keep incrementing left pointer
TIME: O(N), traversing through array
SPACE: O(N), set used to check duplicates
'''
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s: return 0
    left, right, l = 0, 0, len(s)
    char_set, max_ss_size = set(), float('-inf')

    while right < l:
        while s[right] in char_set:                         # remove duplicate
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])                              # add incoming char to set
        max_ss_size = max(max_ss_size, right - left + 1)    # chek max_substring size
        right += 1                                          # increment right pointer

    return max_ss_size