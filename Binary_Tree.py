class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data <= root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
        return root

    def min(self, root):
        if root is None:
            return
        cur = root
        while cur.left is not None:
            cur = cur.left
        return cur.data

    def max(self, root):
        if root is None:
            return
        cur = root
        while cur.right is not None:
            cur = cur.right
        return cur.data

   # def delete(self, root, key):

    def search(self, root, key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.data)
        if root.right is not None:
            self.inorder(root.right)

    def postorder(self, root):
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        print(root.data)

    def travel(self, root):
        if root is None:
            return
        q = [root]
        while q:
            current = q[0]
            Node(current)
            if current.left:
                q.append(current.left)
            print(current.data)
            if current.right:
                q.append(current.right)
            q.pop(0)

if __name__ == '__main__':
    bst = BST()
    print("__________")
    while True:
        val = int(input("Key:"))
        if val == 0:
            break
        bst.insert(bst.root, val)
    print("__________")
    print("Nodes:")
    print("root:", bst.root.data)
    bst.inorder(bst.root)
    print("__________")
    a = int(input("Key:"))
    if bst.search(bst.root, a):
        print("Found")
    else:
        print("Not Found")
    print("__________")
    print("min:", bst.min(bst.root))
    print("max:", bst.max(bst.root))
    bst.travel(bst.root)
