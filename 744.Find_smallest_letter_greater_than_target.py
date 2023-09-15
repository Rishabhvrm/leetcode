
def nextGreatestLetter(letters, target):
    
    ## APPROACH 1 
    ## T(N) = O(N)
    ## SPACE = O(1)

    # traverse array
    # return first greater char than target
    # for ele in letters:
    #     if ele > target:
    #         return ele

    # # if traversed whole list and found no greater char
    # # return first char   
    # return letters[0]

    ## APPROACH 2
    ## BINARY SEARCH - CLUE: SORTED ARRAY
    ## T(N) = O(log n)
    ## SPACE = O(1)
    l, r = 0, len(letters) - 1

    # edge case
    if target < letters[l] or target > letters[r]:
        return letters[0]

    while l+1 < r:
        mid = (l+r) // 2
        if letters[mid] <= target:
            l = mid
        else:
            r = mid
    # return right pointer when found a range - return bigger number
    # if found target, return the next number
    # bc
    return letters[r]

