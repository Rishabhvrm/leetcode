from collections import defaultdict
class Solution:
    '''
    1 2 3 4 5 6 7 8 9 10 11 12 13
    #
    1: [1, 10]
    2: [2, 11]
    3: [3, 12]
    4: [4, 13]
    5: [5]
    6: [6]
    7: [7]
    8: [8]
    9: [9]


    '''
    def countLargestGroup(self, n: int) -> int:

        def sum_of_digits(num):
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        max_size = 0
        sum_group = defaultdict(list)
        res = 0

        for i in range(1, n + 1):
            x = sum_of_digits(i)
            sum_group[x].append(i)
            max_size = max(max_size, len(sum_group[x]))

        for v in sum_group.values():
            if len(v) == max_size:
                res += 1
        
        return res