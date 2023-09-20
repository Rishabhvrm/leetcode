# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if subtree is null
        if not subRoot: return True

        # check if main tree is null
        if not root: return False

        # check if both are same
        if self.sameTree(root, subRoot):
            return True

        # recursively check if left or right subtree is same to the given subtree
        return (self.isSubtree(root.left, subRoot) 
                or self.isSubtree(root.right, subRoot))

    def sameTree(self, t, st):
        # if both null then same
        if not t and not st:
            return True

        # if both exist and have same value, check children
        if t and st and t.val == st.val:
            return self.sameTree(t.left, st.left) and self.sameTree(t.right, st.right)
        
        # return false if both are not same
        return False
