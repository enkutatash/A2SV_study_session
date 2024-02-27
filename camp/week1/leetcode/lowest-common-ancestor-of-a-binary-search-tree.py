# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
            
        def ancestor(root,p,q):
            if root.val<p.val:
                return ancestor(root.right,p,q)
            elif root.val == p.val:
                return root
            elif root.val == q.val:
                return root
            elif p.val< root.val < q.val:
                return root
            else:
                return ancestor(root.left,p,q)
        if p.val>q.val:
            lowestAncestor = ancestor(root, q, p)
            return lowestAncestor
        else:
            lowestAncestor = ancestor(root, p, q)
            return lowestAncestor
        
        
            
        