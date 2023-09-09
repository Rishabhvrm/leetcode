# https://leetcode.com/problems/counting-bits/
    
def countBits(n):
    
    ## BRUTE FORCE
    ## ACCEPTED - BEATS 70% 
    ans = []

    # fill array with 0 to i+1 numbers
    for i in range(n+1):
        ans.append(i)

    for i in range(n+1):
        # bin() returns a string of binary representation 
        # count occurances of 1 in above binary representation
        ans[i] = bin(ans[i]).count('1')

    return ans

def countBits2(n):
    ## DP
    ## A) WITH BIT MANIPULATION
    ## B) WITH OFFSET

    ## A)
    res = [0] * (n+1)
    # right shift and add 1 for values where least significant bit is 1
    for i in range(1, n+1):
        res[i] = res[i >> 1] + (i & 1)
    return res

print(countBits(5))
print(countBits2(5))