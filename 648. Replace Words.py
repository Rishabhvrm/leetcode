from typing import List
class Solution:
    '''
    Approach: Brute Force
    Time: O(dict len * sentence len * avg-word len in dict (for startswith) )
    '''
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        
        for root in dictionary:
            for idx, derivative in enumerate(sentence):
                if derivative.startswith(root):
                    sentence[idx] = root

        return " ".join(sentence)

    '''
    Approach: Using Hashset
    Time: O(d⋅w+s⋅w ^ 2)
    '''
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        sentence = sentence.split(" ")

        def helper(word):
            for i in range(len(word)):
                root = word[:i]
                if root in dict_set:        # root present in dict
                    return root
            # root not present in dict
            return word

        for idx, word in enumerate(sentence):
            sentence[idx] = helper(word)

        return " ".join(sentence)