# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(right,left):
            if right and left:
                if right.val!=left.val :
                    return False
                return symmetric(left.left,right.right) and symmetric(right.left,left.right)
            elif (right and left==None ) or (left and right==None):
                return False
            else:
                return True
        return symmetric(root.left,root.right)
         