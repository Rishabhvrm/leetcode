class Solution:
    "()))(("
    
    '''
    Approach: same as above but without extra space
    O(n): O(n)
    Space: O(1)
    '''
    def minAddToMakeValid(self, s: str) -> int:
        stack_count, count = 0, 0
        for c in s:
            if c == "(":
                stack_count += 1
            elif stack_count and c == ")":
                stack_count -= 1
            else: 
                count += 1
             
        return stack_count + count
    
    '''
    Approach: using stack and keeping count of unmatched closing parenthesis 
    O(n): O(n)
    Space: O(1)
    '''
    def minAddToMakeValid(self, s: str) -> int:
        stack, count = [], 0
        for c in s:
            if c == "(":
                stack.append(c)
            elif stack and c == ")":      # matched
                stack.pop()
            else: 
                count += 1                # unmatched closing parenthesis
             
        #   whatever is unmatched, we're gonna need that many
        #   parenthesis to match it
        return len(stack) + count         