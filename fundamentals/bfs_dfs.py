from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
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


def bfs(root):
    if not root: return []

    result = []
    queue = deque([root])

    # at a given time, q will hold a certain whole level of the tree
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    return result
    

def dfs(root):
    if not root: return

    result.append(root.val)
    dfs(root.left)
    dfs(root.right)


print(bfs(root))
result = []
dfs(root)
print(result)
