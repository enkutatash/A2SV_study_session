# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        p=0
        k=k
        def  small(root):
            nonlocal p,k

            if root:
                l = small(root.left)
                if l != -1:
                    return l
                p+=1
                if p==k:
                    return root.val
                r = small(root.right)
                if r != -1:
                    return r
            return -1
        z=small(root)
        return z

            
