class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_node(self.root, data)

    def _add_node(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._add_node(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._add_node(current.right, data)

    def pre_order_print(self, node):
        if node is None:
            return
        print(node.data, end=" | ")
        self.pre_order_print(node.left)
        self.pre_order_print(node.right)

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.data, end=" | ")
        self.in_order_print(node.right)

    def post_order_print(self, node):
        if node is None:
            return
        self.post_order_print(node.left)
        self.post_order_print(node.right)
        print(node.data, end=" | ")

    def level_order_print(self, node):
        if node is None:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data, end=" | ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def get_root(self):
        return self.root


if __name__ == "__main__":
    nodes = [13, 4, 9, 6, 23, 27, 21, 22, 15, 3, 2, 7]
    bst = BinaryTree()
    for node in nodes:
        bst.add_node(node)

    print("::__Pre Order Traversal__::")
    bst.pre_order_print(bst.get_root())
    print()

    print("::__In Order Traversal__::")
    bst.in_order_print(bst.get_root())
    print()

    print("::__Post Order Traversal__::")
    bst.post_order_print(bst.get_root())
    print()

    print("::__Level Order Traversal__::")
    bst.level_order_print(bst.get_root())
    print()
