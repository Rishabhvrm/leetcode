class Solution:
    '''
    Approach: Using Stack, think STACK whenever you see "(" or ")"
    put the temp list back on the stack
    T(n) = O(n ** 2) => O(n * m)
    n: len of input
    m: # of pairs of parenthesis
    '''
    def reverseParentheses(self, s: str) -> str:
        stack, temp_lst = [], []

        for char in s:
            if char == ")":
                while stack and stack[-1] != "(":
                    temp_lst.append(stack.pop())        # pop from stack and keep it in a temp list
                stack.pop()                             # remove the remaining "("
                
                stack.extend(temp_lst)                  # put the temp list back on the stack
                # or use below instead of above line
                # for ele in temp_lst:
                #     stack.append(ele)
                temp_lst = []                           # reset the temp list for next one   
            else:
                stack.append(char)
                
            
        return "".join(stack)

    '''
    Approach: Wormhole
    map position of "(" with ")"
    jump from "(" to ")" and vice versa and switch directions every time you jump
    T(n) = O(n)
    n: len of input
    '''
    def reverseParentheses(self, s: str) -> str:

        stack, pairs_pos = [], {}
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                pairs_pos[i] = j
                pairs_pos[j] = i


        res = []
        i, direction = 0, 1                                    # 1 => Left to Right, -1 => R to L

        while i < len(s):
            if s[i] == "(" or s[i] == ")":
                i = pairs_pos[i]                               # jump
                direction = -direction                         # change direction
            else:
                res.append(s[i])
            
            i += direction                                     # move based on direction

        return "".join(res)
