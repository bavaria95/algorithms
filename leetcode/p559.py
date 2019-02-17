"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0

        if not len(node.children):
            return 1

        return max([self.dfs(kid) for kid in node.children]) + 1
