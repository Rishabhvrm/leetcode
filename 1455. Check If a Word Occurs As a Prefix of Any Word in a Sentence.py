class Solution:
    '''
    approach: brute force using built-in
    time: O(n * m), n: words in sentence, m: avg len of words
    '''
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")

        for idx, word in enumerate(sentence):
            if word.startswith(searchWord):
                return idx + 1

        return -1