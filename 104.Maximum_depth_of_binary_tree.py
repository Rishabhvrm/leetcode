# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ## TIME COMPLEXITY: O(N)
        ## SPACE COMPLEXITY: O(1)
        ##                 : O(N) if consider recursion stack

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # def count_nodes(node, node_count):
            # if no node, return 0
            # if not node:
            #     return 0

            # # increase node_count as soon as encounter a node
            # node_count += 1

            # # return node_count when encounter leaf node
            # if not node.left and not node.right:
            #     return node_count
            
            # # calculate node_count for left and right subtrees
            # return max(count_nodes(node.left, node_count), 
            #             count_nodes(node.right, node_count))


        # return count_nodes(root, 0)
        