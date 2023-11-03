# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root: return None

        if root == p or root == q: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # p and q are in different subtrees
        # we receive non null values from both children => curr node is LCA
        if l and r: return root

        return l or r
        # for current node we will receive non None values from 1 side and None from the other
        # meaning both p and q lies in left OR right child 
        # in which case, the returning non None value will be the LCA
        # p is a descendant of q => q is LCA
        # q is a descendant of p => p is LCA
