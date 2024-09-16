from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        not_allowed_count = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    not_allowed_count += 1
                    break

        return len(words) - not_allowed_count