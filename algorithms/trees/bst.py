from functools import total_ordering

@total_ordering
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return 'Node: {}'.format(self.key)


class BSTree(object):
    def __init__(self):
        self.root = None

    def _search(self, node, key):
        if not node:
            return None

        if node.key == key:
            return node

        if key < node.key:
            # search in the left subtree
            return self._search(node.left, key)

        return self._search(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _insert(self, root, node):
        if node < root:
            # insert to the left subtree
            if not root.left:
                # if no left subtree - append there
                root.left = node
                return
            # otherwise keep going till reach node with no left leaf
            self._insert(root.left, node)
        else:
            # insert to the right subtree
            if not root.right:
                root.right = node
                return
            self._insert(root.right, node)

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)


if __name__ == '__main__':
    import random

    tree = BSTree()

    nums = list(range(20))
    random.shuffle(nums)

    for i in nums:
        tree.insert(TreeNode(i))

    assert tree.search(0).key == 0
    assert tree.search(10).key == 10
    assert tree.search(25) is None
