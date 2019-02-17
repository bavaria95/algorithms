# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node):
        # in-order
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
            

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = self.dfs(root) # already sorted
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                return True

            if s > k:
                r -= 1
            
            if s < k:
                l += 1
        
        return False
