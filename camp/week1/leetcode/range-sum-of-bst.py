# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sumup = 0

        def traverse(root):
            nonlocal high,low,sumup
            if root:
                if low<= root.val <=high:
                    sumup+= root.val
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return sumup