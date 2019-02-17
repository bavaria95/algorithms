# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def compare_nodes(self, p, q):
        if bool(p) ^ bool(q):
            return False

        if not p and not q:
            return True
        
        return p.val == q.val
        
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        p_queue = [p]
        q_queue = [q]

        while p_queue:
            p = p_queue.pop(0)
            if not q_queue:
                print('nothing in q_queue')
                return False
            q = q_queue.pop(0)
            
            if p is None and q is None:
                return True

            if not self.compare_nodes(p, q):
                return False
            
            if not self.compare_nodes(p.left, q.left):
                return False
            
            if not self.compare_nodes(p.right, q.right):
                return False
        
            if p.left:
                p_queue.append(p.left)
                q_queue.append(q.left)

            if p.right:
                p_queue.append(p.right)
                q_queue.append(q.right)

        return True
