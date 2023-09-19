# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## TIME AND SPACE COMPLEXITY: O(N + M)
        ## TRAVERSING BOTH TREES AND CREATING A NEW TREE

        ## Approach: Create a new tree node, add values to it (and children) while simultaneously traversing the given 2 trees (recursively)

        if not root1 and not root2:
            return None

        # assign value if node exist else assign 0
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        # create a new tree node
        # assign value to new node (val1+val2)
        node = TreeNode(val = val1 + val2)

        # assign left and right children to new node
        # by merging left and right children of given trees
        # this will return a node or a tree that will be assigned as a 
        # left/right child to the node 
        node.left = self.mergeTrees(
            root1.left if root1 else None, 
            root2.left if root2 else None)
        
        node.right = self.mergeTrees(
            root1.right if root1 else None,
            root2.right if root2 else None)

        # return newly created node/tree
        return node