from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    find the path from root to s
    find the path from root to t
    trim the common prefix till LCA (Lowest common ancestor) from the paths 
        - by finding out the idx of first mismatch btw s_path and t_path
    in s_path, len(whole_path) - LCA_idx = # of U
    traverse the t_path to figure out R or L for remaining values of result


    '''
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = []
        curr_path_for_s = []
        curr_path_for_t = []

        def dfs(node, target, curr_path):
            if not node:
                return 

            if node.val == target:
                return curr_path

            curr_path.append("L")
            if dfs(node.left, target, curr_path):
                return curr_path
            curr_path.pop()

            curr_path.append("R")
            if dfs(node.right, target, curr_path):
                return curr_path
            curr_path.pop()

        curr_path_for_s = dfs(root, startValue, [])
        curr_path_for_t = dfs(root, destValue, [])
        
        i = 0 # LCA_idx
        # eliminate the common prefix
        while i < len(curr_path_for_s) and i < len(curr_path_for_t) and curr_path_for_s[i] == curr_path_for_t[i]:
            i += 1
        
        # A B 5 1 3
        #     * 
        LCA_idx = i
        res.extend("U" * (len(curr_path_for_s) - LCA_idx))
        res.extend(curr_path_for_t[LCA_idx : ])
        return "".join(res)
        