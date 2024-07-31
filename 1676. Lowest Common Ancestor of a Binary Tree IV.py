'''
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.

Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
       #
    3 1
    

    3 5 2 7
    3 6
    3 5 2
    3 5 2 4
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        seen = set(nodes)

        def _dfs(node):
            if not node:
                return None

            if node in seen:
                return node
                
            left = _dfs(node.left)
            right = _dfs(node.right)

            if left and right:
                return node

            if left and not right:
                return left

            if not left and right:
                return right
            
            
        return _dfs(root)