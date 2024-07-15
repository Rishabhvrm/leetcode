from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
class Solution:
    '''
    [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    
    all_children:
    {
        15, 17, 20, 80, 19
    }
    nodes:
    {
        20: TreeNode(20),
        15: TreeNode(15),
        17: TreeNode(17),
        50: TreeNode(50),
        80: TreeNode(80),
        19: TreeNode(19)
    }
    '''
    '''
    Approach: hashmap int_node_val : TreeNode(int_node_val)
    make tree by picking up nodes from map and assigning left and right child
    to find the root, pick the node that's not in children set
    Time: O(n)
    Space: O(n)
    '''
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        all_children = set()
        nodes = {}
        
        for p, c, isL in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            
            all_children.add(c)

            tree_node = nodes[p]
            if isL:
                tree_node.left = nodes[c]
            else:
                tree_node.right = nodes[c]

        # to find the root, pick the node that's not in children set
        for k, v in nodes.items():
            if k not in all_children:
                return v