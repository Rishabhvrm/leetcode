class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        out = []

        # flip the second word and merge
        # eg: 'abc' and '123' -> 'abc321'
        # then use 2 pointers to traverse from start and end and add to output
        merge = word1 + word2[::-1]
        l1, lm = len(word1), len(merge)

        # points to first element and j points to last element
        i, j = 0, lm - 1
        
        for _ in range(lm):
            # i will go till the length of first word
            if i < l1:
                out.append(merge[i])
                i += 1

            # j will read the second word in reverse
            # till j is greater than the first word
            if j >= l1:
                out.append(merge[j])
                j -= 1

        return (''.join(out))


# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75