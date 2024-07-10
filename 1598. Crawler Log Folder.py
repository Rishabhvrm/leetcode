from typing import List
class Solution:
    '''
    ./
    x/ => x : [a-z1-9]
    ../
    
    first idea: simulate the problem
    track the path and then see how far is it from the root (start)
    maybe a number line sort of thing
    if see ./ => add 0
    if see ../ => subtract 1
    else => add 1
    wherever you end after traversing logs, you can see how far is it from 0

    logs = ["d1/","d2/","./","d3/","../","d31/"]
        0   1       2.   2     3    2       3

      ["d1/","../","../","../"]
    0   1       0   -1.   -2  

    "d1/","d2/","../","d21/","./"
0      1.  2.    1.     2.    2

    Failed test case:
    ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
0      0    1      0    1       0   0       1   2

    Approach: Simulation and counter
    Time: O(n)
    Space: O(1)

    '''
    def minOperations(self, logs: List[str]) -> int:
        pos = 0

        for log in logs:
            if log == "../":
                # pos = 0 if pos == 0 else (pos - 1)
                pos = max(0, pos - 1)
            elif log == "./":
                pos += 0
            else:
                pos += 1
        
        return 0 if pos < 0 else pos

    '''
    Approach: Stack
    Time: O(n)
    Space: O(n)
    '''
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)

        return len(stack)