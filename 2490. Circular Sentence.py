class Solution:
    '''
    Approach: Split and check
    Time: O(N)
    Space: O(N)
    '''
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        # check the last char of last word and first char of first word
        if words[-1][-1] != words[0][0]:
            return False

        # check the last char of each word with the first char of next word
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False

        return True