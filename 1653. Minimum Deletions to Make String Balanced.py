'''
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
'''
class Solution:
    '''
 B  00011233 
    aababbab 
 A  32211100
     i

    a, ab
    b, ba
    
    aa_a_b_b
    '''
    '''
    Approach: at every i, 
    deletions[i] = a_count_right[i] + b_count_left[i]
    min(deletions)
    Time: O(n)
    Space: O(n)
    '''
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        min_deletion_count = N
        a_count_right = [0 for _ in range(N)]

        # fill up a_count_right
        for i in range(N - 2, -1, -1):
            is_a = 1 if s[i + 1] == "a" else 0
            a_count_right[i] = a_count_right[i + 1] + is_a

        # calculate deletions
        for i in range(N):
            if i == 0:
                b_count_left = 0
            else:
                is_b = 1 if s[i - 1] == "b" else 0
                b_count_left = b_count_left + is_b
            curr_del_count = b_count_left + a_count_right[i]
            min_deletion_count = min(min_deletion_count, curr_del_count)

        return min_deletion_count

    '''
    Approach-2: same as above, using constant space
    Time: O(n)
    Space: O(n)
    '''
    def minimumDeletions(self, s: str) -> int:
        res = float('inf')

        a_count_right = 0
        for c in s:
            a_count_right += 1 if c == "a" else 0

        b_count_left = 0
        for i, c in enumerate(s):
            if c == "a":
                a_count_right -= 1
            
            curr_deletions = b_count_left + a_count_right
            res = min(res, curr_deletions)

            if c == "b":
                b_count_left += 1
        
        return res

    '''
    Approach-3: Using stack
    Time: O(n)
    Space: O(n) 
    '''
    def minimumDeletions(self, s: str) -> int:
        res = 0
        stack = []
        top = -1

        for c in s:
            if c == "a" and stack and stack[top] == "b":
                res += 1
                stack.pop()
            else:
                stack.append(c)

        return res