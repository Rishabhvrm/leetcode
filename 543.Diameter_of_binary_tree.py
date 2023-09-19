# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        ## TIME COMPLEXITY: O(N)
        ## SPACE COMPLEXITY: O(1)
        ##                 : O(N) if consider recursion stack

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # uses the same concept as in
        # https://leetcode.com/problems/maximum-depth-of-binary-tree/
        # calculate diameter using left_depth + right_depth

        def dfs(node):
            nonlocal max_D
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # calculate depth
            max_D = max(max_D, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        max_D = 0
        dfs(root)
        return max_D