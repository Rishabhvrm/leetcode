class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ## APPROACH-1: 
        ## TIME: O(n), traversing front and back
        ## SPACE: O(n), 2 extra lists
        
        # first pass => left to right
        # count extra ")" and skip
        # ls_s = list(s)
        # count_o, count_c = 0, 0             # open and close parenthesis count
        # ls_1, ls_2 = [], []

        # for char in ls_s:
        #     if char == "(": count_o += 1
        #     elif char == ")":
        #         if count_o >= 1: count_o -= 1
        #         else:                       # there are no matching "(", skip this ")" char
        #             continue                # ls_s.pop(i)
        #     ls_1.append(char)               # ls_1 would not contain any extra ")"
        
        # # another pass => right to left
        # # count extra "(" and skip
        # ls_1 = ls_1[::-1]
        # for char in ls_1:
        #     if char == ")": count_c += 1
        #     elif char == "(": 
        #         if count_c >= 1: count_c -= 1
        #         else:                       # there are no matching ")", skip this "(" char
        #             continue
        #     ls_2.append(char)      # ls_2 would not contain any extra "("


        # return "".join(ls_2[::-1])
    

        ## APPROACH-2: use stack for idx of unmatched parenthesis
        ## push idx of "(" on stack, not the "(" itself
        ## and mark indexes for removal
        ## TIME: O(n), traversing front and back
        ## SPACE: O(n), 2 extra lists
        s = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == "(": stack.append(i)
            elif char == ")":
                if stack: stack.pop()           # pop matching parenthesis
                else: s[i] = ''                 # mark this ")" for removal

        # mark "(" for removal
        while stack:
            # print(stack.pop())
            s[stack.pop()] = ''

        return "".join(s)
 


s = ")lee(t(c)o)de)("
s = "))(()"
obj = Solution()
print(s)
print(obj.minRemoveToMakeValid(s))