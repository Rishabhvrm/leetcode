class Solution:
    def is_palindrome(self, string):
            return string == string[::-1]

    def longestPalindrome(self, s: str) -> str:
        
        ## APPROACH: pick every substr & check if it's a palindrome,
        ## if yes, then store it & pick the one with max len
        ## TIME: O ( n * n * n ), for loops and is_palindrome
        ## SPACE: O( n )
        
        def longest_substring(lst):
            max_len, max_str = 0, ""
            for ele in lst:
                if len(ele) > max_len: max_len, max_str = len(ele), ele
            return max_str

        l, res = len(s), []
        for i in range(l):
            for j in range(i,l):
                substring = s[i : j + 1]
                if self.is_palindrome(substring): res.append(substring)
        
        return longest_substring(res)


    ## APPROACH-2: expand outwards at each idx
    ## TIME: O ( n * n )
    ## SPACE: O( n )
    def longestPalindrome2(self, s):
        res, res_len, l = "", 0, len(s)
        flag = "even"
        if l % 2 : flag = 'odd'

        for i in range(l):
            # reset l and r pointers
            if flag == 'odd': left, right = i, i       # odd length
            else: left, right = i, i + 1               # even length
            
            # traverse outward from ith index
            while left >= 0 and right < l and s[left] == s[right]:
                # if found a longer substring palindrome
                if (right - left + 1) > res_len:     
                    res = s[left : right + 1]          # update res and res_len
                    res_len = right - left + 1
                
                left -= 1                              # shift pointers                          
                right += 1
        
        return res

obj = Solution()
s1 = "1312134"
s2 = "babad"
s3 = "cbbd"

print(obj.longestPalindrome(s1))
print(obj.longestPalindrome(s2))
print(obj.longestPalindrome(s3))
print()
print(obj.longestPalindrome2('ac'))
print(obj.longestPalindrome2(s1))
print(obj.longestPalindrome2(s2))
print(obj.longestPalindrome2(s3))