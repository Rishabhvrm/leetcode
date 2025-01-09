from typing import List

class Solution:
    '''
    Approach: Brute force using in-built method
    Time: O(n * m), n: len of words, m: len of pref
    '''
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            # count += 1 if w.startswith(pref) else 0
            count += w.startswith(pref)

        return count