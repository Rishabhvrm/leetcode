from typing import List
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        
        s1 = s1.split(" ")
        for s in s1:
            s1_dict[s] += 1
        
        s2 = s2.split(" ")
        for s in s2:
            s2_dict[s] += 1

        res = []

        # only pick words where freq is 1 and it's not in the other dict
        for ele in s1_dict:
            if s1_dict[ele] == 1 and ele not in s2_dict:
                res.append(ele)
        for ele in s2_dict:
            if s2_dict[ele] == 1 and ele not in s1_dict:
                res.append(ele)

        return res

    '''
    Approach: every uncommon word must occur only once
    store the count of every word in s1 + s2
    '''
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = defaultdict(int)
        s1, s2 = s1.split(" "), s2.split(" ")
        res = []

        for ele in s1 + s2:
            word_count[ele] += 1

        for k, v in word_count.items():
            if v == 1:
                res.append(k)
        
        return res