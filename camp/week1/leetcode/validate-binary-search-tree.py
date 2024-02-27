# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,min,max):
            if root==None:
                return True
            if root.left and root.left.val>=root.val:
                return False
            if root.right and root.right.val<=root.val:
                return False
            if root.val<=min:
                return False
            if root.val>=max:
                return False
            return valid(root.left,min,root.val) and valid(root.right,root.val,max)
        return valid(root,float('-inf'),float('inf'))
            

        