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


    

print(countBits(5))