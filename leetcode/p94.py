# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def dfs(self, node, a):
#         if not node:
#             return
        
#         self.dfs(node.left, a)
#         a.append(node.val)
#         self.dfs(node.right, a)
        
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         a = []
#         self.dfs(root, a)
#         return a



class Solution(object):
    def dfs(self, node):
        q = []
        result = []
        
        while q or node:
            if node:
                q.append(node)
                node = node.left
            else:
                node = q.pop()
                result.append(node.val)
                node = node.right
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.dfs(root)
