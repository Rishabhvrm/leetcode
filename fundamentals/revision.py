'''
----------------------------------------------------------------------------
REVISION: BFS, DFS
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)



def dfs(root):
    if not root: return
    dfs_res.append(root.val)
    dfs(root.left)
    dfs(root.right)


from collections import deque
def bfs(root):
    if not root: return []

    result = []
    q = deque([root])

    # at a given time, q will hold a certain whole level of the tree
    while q:
        level_size = len(q)
        curr_level = []

        for _ in range(level_size):
            curr_node = q.popleft()
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            curr_level.append(curr_node.val)

        result.append(curr_level)
    return result

print("\n---------------------------\nbfs():")
print(bfs(root))
dfs_res = []
dfs(root)
print("\n---------------------------\ndfs():")
print(dfs_res)

'''
----------------------------------------------------------------------------
'''