# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colsIdentify = defaultdict(list)
        
        def traverse(root,row,coln):
            if root:
                row+=1
                colsIdentify[(row,coln)].append(root.val)
                traverse(root.left,row,coln-1)
                traverse(root.right,row,coln+1)


        traverse(root,-1,0)
        sortedBYrow=dict(sorted(colsIdentify.items(), key=lambda a:a[0]))
        sortedBYcol = defaultdict(list)
        for i, v in sortedBYrow.items():
            v.sort()
            sortedBYcol[i[1]].extend(v)
        sorted_dict=dict(sorted(sortedBYcol.items()))
        return sorted_dict.values()