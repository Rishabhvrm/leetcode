class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ele in s:
            # add, if encounter opening paranthesis
            if ele in ['(', '{', '[']:              
                stack.append(ele)

            # if encounter closing paranthesis
            else:
                # if stack is empty
                if not stack:
                    return False
                # pop, top of stack has open paranthesis
                elif ele == ')' and '(' == stack[-1]:       
                    stack.pop()
                elif ele == '}' and '{' == stack[-1]:
                    stack.pop()
                elif ele == ']' and '[' == stack[-1]:
                    stack.pop()
                # top of stack is not open paranthesis
                else:
                    return False   

        # return True if stack is empty, else False
        return True if not stack else False  

# https://leetcode.com/problems/valid-parentheses/