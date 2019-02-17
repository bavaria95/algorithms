# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1

        if node.left:
            left_height = self.dfs(node.left)
        else:
            left_height = 0

        if node.right:
            right_height = self.dfs(node.right)
        else:
            right_height = 0

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.dfs(root) == -1:
            return False
        return True
