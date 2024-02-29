# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        sumAll = 0

        def traverse(root):
            nonlocal sumAll
            if root ==None:
                return

            if root and root.right == None and root.left == None:
                numbers.append(str(root.val))
                result= "".join(numbers)
                # print("insert",numbers,root.val)
                sumAll+=int(result)
                print(result)
                
            else:
                numbers.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
            if len(numbers)>0:
                numbers.pop()
            
        traverse(root)
        return sumAll


            
            

            
        
