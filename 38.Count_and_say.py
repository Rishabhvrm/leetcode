from collections import Counter
class Solution:
    def countAndSay(self, n: int) -> str:

        # a) # count, number = function to count unique digits in given number
        # b) # 2,1 => 21, keep appending to the list
       
        if n == 1: return "1"

        result = "1"
        
        for _ in range(n - 1):
            # store output for every digit
            # i.e. freq and digit
            say = []
            idx = 0
            
            while idx < len(result):
                # counts freq of digit
                # every digit will have atleast 1 count
                count = 1                   

                # count same digit
                while idx < len(result) - 1 and result[idx] == result[idx + 1]:
                    count += 1
                    idx += 1
                
                # add to list
                say.append(str(count) + result[idx])
                idx += 1
            
            result = ''.join(say)

        return result


s = Solution()
print(s.countAndSay(5))