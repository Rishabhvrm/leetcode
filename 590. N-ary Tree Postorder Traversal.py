
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def _dfs(node):
            if not node:
                return

            for c in node.children:
                _dfs(c)
            
            res.append(node.val)

        res = []
        _dfs(root)
        return res