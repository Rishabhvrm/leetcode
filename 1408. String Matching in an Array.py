from typing import List
class Solution:
    '''
    "a", "aa", "aaa", "aba", "aababa"
    '''
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        res.add(words[i])

        return list(res)