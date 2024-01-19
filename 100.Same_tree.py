# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        
        ## TIME COMPLEXITY: O(P+Q) => O(N)
        ## SPACE COMPLEXITY: O(1), O(N) if consider recursion stack
        
        # base case: both are empty => same tree
        if not p and not q:
            return True

        # if one is empty and other isn't => different trees
        if not p or not q:
            return False

        # if values don't match for same node => different trees
        if p.val != q.val:
            return False

        # recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        if not p or not q: return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)