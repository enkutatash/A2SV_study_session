# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(l,r):
            if l > r: 
                return None
            mid = (l+r)//2
            left= BST(l,mid-1)
            right = BST(mid+1,r)
            return TreeNode(nums[mid],left,right)
        return BST(0,len(nums)-1)
            
        
        