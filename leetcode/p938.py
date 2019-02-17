# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, L, R):
        q = [root]
        s = 0

        while q:
            node = q.pop()
            if L <= node.val <= R:
                s += node.val
            
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return s
        

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return self.dfs(root, L, R)
