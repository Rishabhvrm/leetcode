class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        
        s = list(s)
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                s[i] = chr(ord(s[i]) + 32)

        return ''.join(s)
    
obj = Solution()
s = "Hello"
print(obj.toLowerCase(s))