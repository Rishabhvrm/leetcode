from typing import List, Counter
from collections import defaultdict

class Solution:
    '''
    create hashmaps for every word (char -> count)
    see common keys btw these hashmaps and choose min values for those common keys
    '''
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        first_char_occ_map = defaultdict(int)   # char -> occurance

        # build first hashmap
        for char in words[0]:
            first_char_occ_map[char] += 1
            
        for word in words:
            # build hashmap for every word (could skip the first word if want)
            curr_char_occ = defaultdict(int)

            for char in word:
                curr_char_occ[char] += 1
            
            for k in first_char_occ_map:
                # skip chars that are not common, default val will be 0
                # also take min val if key occurs in both maps
                first_char_occ_map[k] = min(first_char_occ_map[k], curr_char_occ[k])
        
        for k, v in first_char_occ_map.items():
            for _ in range(v):
                res.append(k)
        
        return res

    '''
    same as above, just using in-built Counter() for cleaner code
    '''
    def commonChars(self, words: List[str]) -> List[str]:
        base_map = Counter(words[0])    # char -> count/occurance
        res = []
        
        for word in words:
            curr_map = Counter(word)

            # pick common chars with least val btw maps for each word
            for char in base_map:
                base_map[char] = min(base_map[char], curr_map[char])

        for k, v in base_map.items():
            for _ in range(v):
                res.append(k)

        return res        