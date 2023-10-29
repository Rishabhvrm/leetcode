from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ## APPROACH-1: USING % OPERATOR
        ## TIME: O(N)
        ## SPACE: O(N), result array

        # res = []
        # for idx in range(1, n + 1):
        #     if idx % 3 == 0 and idx % 5 == 0:
        #         res.append("FizzBuzz")
        #     elif idx % 5 == 0:
        #         res.append("Buzz")
        #     elif idx % 3 == 0:
        #         res.append("Fizz")
        #     else:
        #         res.append(str(idx))

        # return res

        
        ## APPROACH-2: STRING ARRAY INITIALIZATION 
        ## AND USE OF FOR LOOPS FOR 3, 5, AND 15
        ## TIME: O(N)
        ## SPACE: O(N), result array

        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]

        # place 'Fizz' at multiples of 3 
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr