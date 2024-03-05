# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        distance = defaultdict(lambda : [float('inf'),0])

        def traverse(root,r,c):
            if root :
                distance[r][0]=min(distance[r][0],c)
                distance[r][1]=max(distance[r][1],c)

                traverse(root.left,r+1,2*c)
                traverse(root.right,r+1,2*c+1)
        traverse(root,0,0)
        maxwidth = 0
        for i, v in distance.values():
            maxwidth = max(maxwidth,v-i)
        return maxwidth+1
            

        
        
