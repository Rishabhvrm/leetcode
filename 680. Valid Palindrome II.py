class Solution:
    def check_palindrome(self, a: int, b: int) -> bool:
        s = self.s
        while a <= b:
            if s[a] != s[b]:
                return False
            a, b = a + 1, b - 1
        return True

    def validPalindrome(self, s: str) -> bool:
        self.s = s
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                
                l += 1      # skip s[l]
                skip_left = self.check_palindrome(l, r)
                
                l -= 1      # undo the skipping step
                r -= 1      # skip s[r]
                skip_right = self.check_palindrome(l, r)

                return skip_left or skip_right
            l, r = l + 1, r - 1

        return True     # never found a mismatch

