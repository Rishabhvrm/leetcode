# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        
        ## TIME COMPLEXITY: O(N), visiting every node once
        ## SPACE COMPLEXITY: O(1), since no extra space
        #                  : O(N), if consider recursion stack

        def dfs(node, curr_sum):
            # base case: empty tree => return False
            if not node:
                return False

            # update current sum
            curr_sum += node.val

            # check sum when found a leaf node
            if not node.left and not node.right:
                return curr_sum == targetSum

            # recursively check left and right sub trees
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        # call dfs with current sum = 0
        return dfs(root, 0)