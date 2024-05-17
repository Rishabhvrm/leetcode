# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    '''
    Post Order Traversal 
    Order matters here and return value matters here
    usually, you do bfs in pre-order
    '''
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # check leaf
            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)