# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_list = []
        def IOT(root):
            if root:
                IOT(root.left)
                sorted_list.append(root.val)
                IOT(root.right)
        IOT(root)
        def BST(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            left = BST(l,mid-1)
            right = BST(mid+1,r)
            return TreeNode(sorted_list[mid],left,right)

        return BST(0,len(sorted_list)-1)
        
        