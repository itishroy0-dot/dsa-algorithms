class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# Example
bst = BST()
root = None
for val in [50, 30, 20, 40, 70, 60, 80]:
    root = bst.insert(root, val)
bst.inorder(root)  # 20 30 40 50 60 70 80
