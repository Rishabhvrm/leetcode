from collections import Counter
class Solution:
    '''
    Approach: sliding window using hashmap, compare freq
    get the freq of chars in s1, 
    traverse s2 with a window size equal to s1 and check freq of chars there
    if match, then true
    Time: O(n)
    Space: O(n)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        og_counter = Counter(s1)
        l, r = 0, len(s1)

        while r <= len(s2):
            curr_window = s2[l : r]
            count_curr_window = Counter(curr_window)
            if og_counter == count_curr_window:
                return True
            l, r = l + 1, r + 1

        return False

    '''
    Approach: Same as above, just used an array of size 26 instead of a map
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        s1_char_freq = [0] * 26

        # freq of chars in s1
        for c in s1:
            s1_char_freq[ord(c) - ord('a')] += 1

        # traverse s2 with window size of s1 and check if freq is same as s1
        l = r = 0
        curr_map = [0] * 26

        while r < len(s1):
            curr_map[ord(s2[r]) - ord('a')] += 1
            r += 1

        if s1_char_freq == curr_map:
            return True

        while r < len(s2):
            curr_map[ord(s2[l]) - ord('a')] -= 1
            curr_map[ord(s2[r]) - ord('a')] += 1
            
            if s1_char_freq == curr_map:
                return True

            l += 1
            r += 1

        return False