# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def averageOfLevels(root):
    
    ## TIME COMPLEXITY:  O(N), visiting each node once
    ## SPACE COMPLEXITY: O(M), storing M values at a given point in time
    ## where M is Max number of nodes at any level
    ## Max value for M can be N/2 for a perfectly balanced binary tree
    
    # when encounter null value
    if not root:
        return []

    result = []
    # dequeue for BFS traversal
    # q will contain all the nodes in a level at a given time
    # len(q) will contain number of nodes in a level
    q = deque([root])      

    while q:
        # initialize level count and sum
        l_sum, l_count = 0, len(q)
        
        # traverse level
        for _ in range(l_count):
            node = q.popleft()
            l_sum += node.val

            # check if node has children
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        # store avg
        result.append(l_sum/l_count)
    return result
