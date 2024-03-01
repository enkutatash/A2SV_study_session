# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.exist=defaultdict(int)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                self.exist[root.val]+=1
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        result=[]
        maxi=max(self.exist.values())
        for i,v in self.exist.items():
            if v==maxi:
                result.append(i)
        return result

        