# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # sum_level = defaultdict(list)
        level, max_sum, ans = 1, float('-inf'), 0

        q = deque([root])

        while q:
            q_len = len(q)
            curr_level_sum = 0
            
            for _ in range(q_len):
                curr_node = q.popleft()
                curr_level_sum += curr_node.val
            
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                        
            if curr_level_sum > max_sum:
                max_sum = curr_level_sum
                ans = level
            
            level += 1
        
        return ans
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)

        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            
            level_sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        max_sum = float('-inf')
        res_level = 0

        for k,v in level_sum.items():
            if v > max_sum:
                max_sum = v
                res_level = k
        
        return res_level