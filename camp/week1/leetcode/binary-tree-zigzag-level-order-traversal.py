# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = [[root.val]]
        def levelTraverse(queue, turn):
            if len(queue)==0 :
                return None
            queue2 = deque()
            while queue:
                ele = queue.popleft()
                if ele.left:
                    queue2.append(ele.left)
                if ele.right:
                    queue2.append(ele.right)
            if turn =="rev":
                local=[]
                for i in range(len(queue2)-1,-1,-1):
                    local.append(queue2[i].val)
                result.append(local)
                queue = queue2
                
                return levelTraverse(queue,"forward")
            else:
                local=[]
                for i in queue2:
                    local.append(i.val)
                result.append(local)
                queue = queue2
                
                return levelTraverse(queue,"rev")
        levelTraverse(queue,"rev")
        return result[:-1]

                
