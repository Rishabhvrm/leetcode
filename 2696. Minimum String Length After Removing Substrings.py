class Solution:
    '''
    Brute Force: using string methods
    Time: O(n ** 2)
    Space: O(n)
    '''
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB", "")
            if "CD" in s:
                s = s.replace("CD", "")
            
        return len(s)

    '''
    Approach: using stack
    Time: O(n)
    Space: O(n)
    '''
    def minLength(self, s: str) -> int:
        stack = []
        top = -1

        for char in s:
            if char == "B" and stack and stack[top] == "A":
                stack.pop()
            elif char == "D" and stack and stack[top] == "C":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


