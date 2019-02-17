# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, a):
        if not node:
            return

        self.dfs(node.left, a)
        a.append(node.val)
        self.dfs(node.right, a)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = []
        self.dfs(root, a)
        
        return min([abs(a[i] - a[i+1]) for i in range(len(a) - 1)])
