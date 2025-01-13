from typing import List
from collections import defaultdict, Counter

class Solution:
    '''
    Approach: using hash-maps
    create a map for whole words2 (pick the max occ of a char among words) and 
    check if it's a subset for each ele in words 1, if yes add to res
    Time: O(m * L + n * L), m: len of words2, n: len of words1, L: avg len of each word
    Space: O(1), 26 chars
    '''
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def subset(char_count_a, char_count_b) -> bool:
            for k in char_count_b.keys():
                if char_count_b[k] > char_count_a[k]:
                    return False
            return True
        
        def create_counter_for_2(word2: List[int]) -> str:
            char_freq = defaultdict(int)
            for w in word2:
                curr_map = Counter(w)
                for k,v in curr_map.items():
                    char_freq[k] = max(v, char_freq[k])
            
            return char_freq


        res = []
        word2_counter = create_counter_for_2(words2)

        for i in range(len(words1)):
            word1_counter = Counter(words1[i])

            if subset(word1_counter, word2_counter):
                res.append(words1[i])
                  
        return res

        '''
        take the max occurance 
        cl, odc => cdol
        oo, oa  => ooa 
        '''
