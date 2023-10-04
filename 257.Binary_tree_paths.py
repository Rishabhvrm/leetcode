# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    def dfs(node, current_path):
        # return if none node
        if not node:
            return
        
        # append to path if encounter value
        if node.val is not None:
            current_path += str(node.val)

        # if leaf node, append path to output list
        if not node.left and not node.right:
            paths.append(current_path)
        # not a leaf node, append '->' to path and call func for left and right child
        else:
            current_path += "->"
            dfs(node.left, current_path)
            dfs(node.right, current_path)

    paths = []
    dfs(root, "")
    return paths

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node5


print(binaryTreePaths(node1))



    