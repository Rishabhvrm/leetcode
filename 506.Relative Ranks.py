from typing import List


class Solution:
    '''
    Approach-1: Brute force
    Time: O(n ^ 2)
    Space: O(n), res[]
    '''
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []

        def calculate_score(count):
            if count == len(score) - 1:
                res.append("Gold Medal")
            elif count == len(score) - 2:
                res.append("Silver Medal")
            elif count == len(score) - 3:
                res.append("Bronze Medal")
            else:
                res.append(str(len(score) - count))

        for i in range(len(score)):
            count = 0
            for j in range(len(score)):
                if i != j:
                    if score[i] > score[j]:
                        count += 1
            
            calculate_score(count)

        return res
            
    '''
    Approach-2: Optimized, sorting, hashmap (to store idx)
    Time: O(n * log n)
    Space: O(n), res[]
    '''
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        
        res = []
        score_idx = {}
        
        for i, s in enumerate(sorted_score):
            score_idx[s] = i

        for s in score:
            idx = score_idx[s]
            if idx == 0:
                res.append("Gold Medal")
            elif idx == 1:
                res.append("Silver Medal")
            elif idx == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(idx + 1))

        return res

    '''
    Approach-3: Optimized, hashmap
    Time: O(n)
    Space: O(n), res[]
    '''
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pass