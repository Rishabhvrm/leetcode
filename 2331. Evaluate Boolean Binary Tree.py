# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    '''
    Time: O(n), dfs()
    Space: O(n), recursion stack
    '''
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # leaf node
            if not node.left and not node.right:
                return mapping[node.val]

            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            elif node.val == 3:
                return dfs(node.left) and dfs(node.right)

        mapping = {
            0: False,
            1: True
        }

        return dfs(root)
        