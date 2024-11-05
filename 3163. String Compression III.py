class Solution:
    '''
    Approach: count the chars, add a dummy char at last
    Time: O(N)
    Space: O(N)
    '''
    def compressedString(self, word: str) -> str:
        word += "A"
        comp = ""
        curr_count = 1

        for i in range(1, len(word)):
            if curr_count < 9 and  word[i - 1] == word[i]:
                    curr_count += 1
            else:
                comp += str(curr_count) + word[i - 1]
                curr_count = 1
            
        return comp