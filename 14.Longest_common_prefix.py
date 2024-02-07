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



def longest_common_prefix(strs) -> str:
    if not strs:
        return ""

    # Sort the list of strings
    strs.sort()
    print(strs)

    # Find the common prefix between the first and last string
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

strs =  ["flower","flow","flight", "fl"]    #  Output: "fl"
strs = ["dog","racecar","car"]              #  Output: ""

print(longest_common_prefix(strs))