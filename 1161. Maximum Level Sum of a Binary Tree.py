# Definition for a binary tree node.
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