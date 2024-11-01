class Solution:
    '''
     l
    leeetcode
     r
    0
      --
    XXaabaaa

    '''

    '''
    Approach: Sliding window and marking
    Time: O(N)
    Space: O(N)
    '''
    def makeFancyString(self, s: str) -> str:
        res = []
        s = list(s)

        l, r = 0, 0
        count = 0
        while r < len(s):
            if s[l] == s[r]:
                count += 1
            else:
                l = r
                count = 1

            if count == 3:
                s[l] = "X"
                l += 1
                count -= 1

            r += 1

        for c in s:
            if c != "X":
                res.append(c)

        return "".join(res)

    '''
    Approach: Using Stack
    Time: O(N)
    Space: O(N)
    '''
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            if len(stack) > 1 and stack[-1] == stack[-2] == c:
                stack.pop()
            stack.append(c)

        return "".join(stack)
