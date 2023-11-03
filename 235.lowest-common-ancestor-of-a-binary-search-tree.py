# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # TIME: O(log n)
        # SPACE: O(1)
        curr = root

        # given that p and q will exist in tree
        while curr:
            
            # curr node is less than q and q, check in right subtree (containing larger values)
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # curr node is greater than q and q, check in left subtree (containing smaller values)
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left

            # split occurs (answer), or curr is one of inputs
            else:
                return curr