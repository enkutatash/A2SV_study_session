# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA=countB=0
        currA=headA
        currB=headB
         
        while currA:
            countA+=1
            currA=currA.next
        while currB:
            countB+=1
            currB=currB.next
        cA=headA
        cB=headB
        while countA!=countB:
            if countA>countB:
                countA-=1
                cA=cA.next
            else:
                countB-=1
                cB=cB.next
        
        while cA and cB:
            if cA==cB:
                return cA
            cA=cA.next
            cB=cB.next
        return None
                


        

        