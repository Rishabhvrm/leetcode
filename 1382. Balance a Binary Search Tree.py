# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
    Approach: convert to in-order array, split that array recursively to create a BST
    Time: O(n + n), to create in-order and then to create BST
    Space: O(n), creating a new tree
    '''
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node: return 
            inorder(node.left)
            in_order_arr.append(node.val)
            inorder(node.right)

        
        def create_bst(arr):
            if not arr:
                return None
            
            middle_idx = len(arr) // 2
    
            return TreeNode(arr[middle_idx], 
                    create_bst(arr[ : middle_idx]), 
                    create_bst(arr[middle_idx + 1 : ]))
            
        in_order_arr = []
        inorder(root)                       # create in-order array
        return create_bst(in_order_arr)     # create bst from in-order array

    '''
    Approach: same as above, just coding differently
    Time: O(n + n), to create in-order and then to create BST
    Space: O(n), creating a new tree
    '''
    def balanceBST(self, root: TreeNode) -> TreeNode:
        in_order_arr = []
        self.in_order(root, in_order_arr)
        return self.create_bst(in_order_arr, 0, len(in_order_arr) - 1)

    def in_order(self, node: TreeNode, in_order_arr: list) -> None:
        if not node: return

        self.in_order(node.left, in_order_arr)
        in_order_arr.append(node.val)
        self.in_order(node.right, in_order_arr)

    def create_bst(self, arr: list, left: int, right: int) -> TreeNode:
        if left > right:
            return None

        mid = left + (right - left) // 2

        node = TreeNode(arr[mid])
        node.left = self.create_bst(arr, left, mid - 1)
        node.right = self.create_bst(arr, mid + 1, right)

        return node

