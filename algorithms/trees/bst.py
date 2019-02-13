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
