# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Recursive solution
'''
# class Solution(object):
#     def dfs(self, node, a):
#         if not node:
#             return

#         a.append(node.val)
#         self.dfs(node.left, a)
#         self.dfs(node.right, a)

#     def preorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         a = []
#         self.dfs(root, a)
#         return a


'''
Iterative solution
'''

class Solution(object):
    def dfs(self, node):
        if not node:
            return []

        q = [node]
        result = []
        
        while q:
            node = q.pop()
            result.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.dfs(root)
