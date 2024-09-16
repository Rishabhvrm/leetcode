from typing import List
class Solution:
    '''
    using set
    '''
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        not_allowed_count = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    not_allowed_count += 1
                    break

        return len(words) - not_allowed_count

    '''
    same as above
    '''
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0

        for w in words:
            all_char_present = True
            for c in w:
                if c not in allowed:
                    all_char_present = False
                    break
            if all_char_present:
                count += 1
            
        return count

    '''
    bit manipulation
    set the bits for chars in allowed
    '''
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask, count = 0, 0
        
        # prepare mask
        for c in allowed:
            mask |= (1 << ord(c) - ord('a'))

        for w in words:
            all_char_present = True

            for c in w:
                if (mask >> (ord(c) - ord('a')) & 1) == 0:
                    all_char_present = False
                    break
            
            if all_char_present:
                count += 1

        return count

        
