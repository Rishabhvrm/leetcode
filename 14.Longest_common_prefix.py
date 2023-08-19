# easy
# https://leetcode.com/problems/longest-common-prefix/


    
def longestCommonPrefix(strs) -> str:
    # return empty string if input is empty
        if len(strs) == 0:
            return ""

        base = strs[0]
        # return empty string if base element is empty string
        if base == "":
            return ""

        # travese length of input
        for i in range(len(base)):
            for word in strs[1:]:
                # if any element is shorter than the first element
                # OR
                # found a mismatch
                # then return whatever traversed till then
                if (i == len(word) or word[i] != base[i]):
                    return base[0:i]

        # if base is shorter than other elements
        return base

# ["flower","flow","flight"]
# ["dog","racecar","car"]