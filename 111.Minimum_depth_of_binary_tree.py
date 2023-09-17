# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minDepth(root):
    
    ## TOPIC: TREES, RECURSION, DFS
    ## TIME COMPLEXITY: O(N), EVERY NODE IS VISITED ONCE
    ## SPACE COMPLEXITY: O(1), but can be O(N) if recursion stack is considered

    if not root:
        return 0

    # if one of the subtrees is empy, consider the non-empty subtree
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)
    
    # # If both subtrees are non-empty, return the minimum depth
    return 1 + min(minDepth(root.left), minDepth(root.right)) 
