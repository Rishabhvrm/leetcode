def isSubsequence(s: str, t: str) -> bool:

    # if s is empty or s == t, return true
    if s == "" or s == t:
        return True

    flag = False
    i, j = 0, 0

    # traverse till end
    while i < len(s) and j < len(t):
        # if found match, increment both pointers
        if s[i] == t[j]:
            i += 1
        # if no match found, just increase 'j' pointer
        j += 1
        
        # if i goes out of bound, set flag as true
        if i == len(s): flag = True
    
    return flag

s = "abd"
t = "ahbgdc"

print(isSubsequence(s, t))