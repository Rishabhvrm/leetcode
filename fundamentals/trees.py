# BINARY TREE

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self._insert(self.root, value)

    def search(self, value):
        return self._search(self.root, value)

    # def delete(self, value):
    #     self.root = self._delete(self.root, value)

    # _ : intended for internal use
    def _insert(self, current_node, value):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)                
        else:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def _search(self, current_node, value):
        if current_node:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                return self._search(current_node.left, value)
            elif value > current_node.value:
                return self._search(current_node.right, value)
        return False
    
    def inorder_traversal(self):
        res = []
        self._inorder_traversal(self.root, res)
        return res

    def _inorder_traversal(self, root, res):
        if root:
            self._inorder_traversal(root.left, res)
            res.append(root.value)
            self._inorder_traversal(root.right, res)

    def preorder_traversal(self):
        res = []
        self._preorder_traversal(self.root, res)
        return res

    def _preorder_traversal(self, root, res):
        if root:
            res.append(root.value)
            self._preorder_traversal(root.left, res)
            self._preorder_traversal(root.right, res)


tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
print(tree.inorder_traversal())
print(tree.preorder_traversal())
print(tree.search(3))
print(tree.search(10))
print(tree.search(30))
