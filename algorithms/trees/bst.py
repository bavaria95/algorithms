from functools import total_ordering

@total_ordering
class TreeNode(object):
    def __init__(self, key):
        self.key = key

        self.parent = None
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
                node.parent = root
                return
            # otherwise keep going till reach node with no left leaf
            self._insert(root.left, node)
        else:
            # insert to the right subtree
            if not root.right:
                root.right = node
                node.parent = root
                return
            self._insert(root.right, node)

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _remove_child(self, node):
        parent = node.parent
        if not parent:
            self.root = None
            return

        if parent.left is node:
            parent.left = None

        if parent.right is node:
            parent.right = None

    def remove_by_node(self, node):
        if not node:
            return

        if not node.left and not node.right:
            # no children - just remove it
            self._remove_child(node)
            del node
            return

        if bool(node.left) ^ bool(node.right):
            # if node has only one child

            child = node.left if node.left else node.right

            parent = node.parent
            if not parent:
                self.root = child

            if parent and parent.left is node:
                parent.left = child
            elif parent:
                parent.right = child

            child.parent = parent
            return

        # if both children are present
        # finding successor in-order node
        succ = self.min(node.right)

        # swapping it with node to remove
        self._swap_nodes(node, succ)

        if not succ.parent:
            self.root = succ

        self.remove_by_node(node)
        del node

    def remove(self, key):
        node = self.search(key)
        self.remove_by_node(node)

    def _swap_nodes(self, node1, node2):
        if node1.left:
            node1.left.parent = node2
        if node1.right:
            node1.right.parent = node2

        if node2.left:
            node2.left.parent = node1
        if node2.right:
            node2.right.parent = node1

        if node1.parent and node1.parent.left and node1.parent.left is node1:
            node1.parent.left = node2
        if node1.parent and node1.parent.right and node1.parent.right is node1:
            node1.parent.right = node2
        if node2.parent and node2.parent.left and node2.parent.left is node2:
            node2.parent.left = node1
        if node2.parent and node2.parent.right and node2.parent.right is node2:
            node2.parent.right = node1


        node1.parent, node2.parent = node2.parent, node1.parent
        node1.left, node2.left = node2.left, node1.left
        node1.right, node2.right = node2.right, node1.right


    def min(self, node=None):
        # find the smaller key starting from the node
        # if node is not passed - finds minumum in the whole tree
        if not node:
            it = self.root
        else:
            it = node

        while it.left:
            it = it.left

        return it

    def max(self, node=None):
        # find the smaller key starting from the node
        # if node is not passed - finds minumum in the whole tree
        if not node:
            it = self.root
        else:
            it = node

        while it.right:
            it = it.right

        return it


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

    if tree.root.left:
        assert tree.root is tree.root.left.parent
    else:
        assert tree.root is tree.root.right.parent

    for i in range(20):
        assert bool(tree.search(i))

    for i in range(20):
        tree.remove(i)
        assert not bool(tree.search(i))
