# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=0
        
        def valid(root):
            nonlocal ans
            if root == None:
                return True , 0,float("inf") ,float("-inf")
            validityLeft, sumleft, leftmin, leftmax = valid(root.left)
            validityRight, sumright,rightmin,rightmax = valid(root.right)
            
            if validityLeft and validityRight and leftmax<root.val<rightmin:
                csum=sumleft+sumright+root.val
                ans=max(csum,ans)

                return True ,csum,min(leftmin,root.val),max(rightmax,root.val)
            return False, 0 , 0, 0
       
            
        valid(root)
        
        return ans

            
        