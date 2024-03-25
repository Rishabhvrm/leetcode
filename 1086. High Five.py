'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

 
Example 1:

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
Example 2:

Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]
 

Constraints:

1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.

'''

from typing import List
import heapq

'''
I/O:
    how many students?      => 1 to 1000
    can there be less than 5 entries for a student?     => No, at least 5 scores for each ID
    can input be empty?     => no, 1 to 1000
    repeat ? => wont' matter

    Output: sorted?         => Yep
'''

class Solution:
    '''
    APPROACH: 
        Using Max-heap
        can make a map { ID: max_heap of scores }
        when done traversing, sum top 5 vals from heap and return the avg for each ID
        {
            1: 91, 92, 100, 65, 87  
            2: 93, 97, 77, 100, 76
        }
    
    '''
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_scores = {}

        for id, score in items:
            if id not in id_scores:
                id_scores[id] = [-score]
            else:
                id_scores[id].append(-score)

        res = []
        sorted_keys = sorted(id_scores.keys())  # sort keys
        for id in sorted_keys:
            v = id_scores[id]
            heapq.heapify(v)
            count, total_score = 0, 0

            while count < 5:
                total_score += -heapq.heappop(v)
                count += 1
            res.append([id, (total_score) // 5])    # integer division   
        return res 

    '''
    APPROACH: 
        Using min-heap
        can make a map { ID: min_heap of scores of size 5}
        when done traversing, sum the heap and return the avg for each ID
        {
            1: 91, 92, 100, 65, 87  
            2: 93, 97, 77, 100, 76
        }
    
    '''
    def highFive2(self, items: List[List[int]]) -> List[List[int]]:
        id_scores = {}

        for id, score in items:
            if id not in id_scores:
                min_heap = []
                heapq.heappush(min_heap, score)
                id_scores[id] = min_heap
            else:
                heapq.heappush(id_scores[id], score)
            if len(id_scores[id]) > 5:
                heapq.heappop(id_scores[id])

        res = []
        sorted_student_ids = sorted(id_scores.keys())       # only sort the keys
        for id in sorted_student_ids:
            total_score = 0
            min_heap = id_scores[id]
            while min_heap:
                total_score += heapq.heappop(min_heap)
            res.append([id, total_score // 5])
        return res


items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]   # [[1, 100], [7, 100]]
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]  # [[1, 87], [2, 88]]
# print(Solution().highFive(items));
print(Solution().highFive2(items));

