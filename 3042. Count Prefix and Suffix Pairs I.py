from typing import List
class Solution:
    '''
    words = [a, aba, aa]

    2
    '''
    # def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
    #     # assuming str1 is smaller
    #     if len(str1) > len(str2):
    #         return False

    #     is_prefix, is_suffix = True, True
        
    #     for i in range(len(str1)):
    #         if str1[i] != str2[i]:
    #             is_prefix = False
    #             break

    #     str1, str2 = str1[::-1], str2[::-1]

    #     for i in range(len(str1)):
    #         if str1[i] != str2[i]:
    #             is_suffix = False
    #             break
        
    #     return is_prefix and is_suffix

    def isPrefixAndSuffix(self, str1, str2) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res


        