# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        rootVal=root.val
        maxDiff=0

        def ancestor(root, mini,maxi):
            nonlocal maxDiff
            if root:
                if root.val<mini:
                    mini = root.val
                if root.val>maxi:
                    maxi = root.val
                maxDiff=max(maxDiff ,maxi - mini)
                print(root.val,mini,maxi)
                ancestor(root.left,mini,maxi)
                ancestor(root.right,mini,maxi)
                    

        ancestor(root,root.val,root.val)
        return maxDiff

        