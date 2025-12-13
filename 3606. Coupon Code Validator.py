from typing import List
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        priority = {
            "electronics": 1,
            "grocery": 2, 
            "pharmacy": 3,
            "restaurant": 4
        }

        def is_valid_code(cd):
            return len(cd) > 0 and all(c.isalnum() or c == "_" for c in cd)

        N = len(code)
        res = []

        for i in range(N):
            if (
                isActive[i] and
                businessLine[i] in priority and
                is_valid_code(code[i])
            ):
                res.append([priority[businessLine[i]],code[i]])
        
        res.sort()
        return [b for a, b in res]