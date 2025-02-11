
class Solution:
    '''
    daabcbaabcbc 
               #  
    abc

    dab
    '''
    '''
    very brute force
    t(n): O(N ** 2)
    '''

    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            part_idx = s.find(part)
            s = s[:part_idx] + s[part_idx + len(part):]
        return s

    '''
    using stack
    t(N): O(N)
    space: O(N)

    abcd    ada
    a

         #
    daXXXbaabcbc    abc
    '''
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        
        for c in s:
            stack.append(c)
            part_in_stack_len = 0
        
            if stack and stack[-1] == part[-1]:
                i, j = len(stack) - 1, len(part) - 1
            
                while i >= 0 and j >= 0:
                    if stack[i] == part[j]:
                        part_in_stack_len += 1
                        i, j = i - 1, j - 1
                    else:
                        break

                if part_in_stack_len == len(part):
                    while part_in_stack_len > 0:
                        temp = stack.pop()
                        part_in_stack_len -= 1

        return "".join(stack)
