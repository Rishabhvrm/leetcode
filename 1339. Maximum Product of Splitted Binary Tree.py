from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # find total sum
        def total_sum_dfs(node):
            if not node:
                return 0
            
            return node.val + total_sum_dfs(node.left) + total_sum_dfs(node.right)
        
        # find subtree sum 
        # it's same as the above function
        # we could just write one function
        def find_sum_dfs(node):
            nonlocal max_prod
            if not node:
                return 0

            left_sum = find_sum_dfs(node.left)
            right_sum = find_sum_dfs(node.right)

            subtree_sum = node.val + left_sum + right_sum
            remaining_sum = total_sum - subtree_sum
            
            max_prod = max(max_prod, subtree_sum * remaining_sum)

            return subtree_sum

        MOD = 10**9 + 7
        max_prod = float('-inf')

        total_sum = total_sum_dfs(root)
        find_sum_dfs(root)
        return max_prod % MOD