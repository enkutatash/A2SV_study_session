# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(l,r):
            if l>r:
                return 
            localmax = max(nums[l:r+1])
            maxidx = nums.index(localmax)
            left = build(l,maxidx-1)
            right = build(maxidx +1,r)
            return TreeNode(nums[maxidx],left,right) 
        return build(0,len(nums)-1)
        