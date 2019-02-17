# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0

        if not node.left and not node.right:
            return 1

        return max(self.dfs(node.left), self.dfs(node.right)) + 1

        
