# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseL(head):
            prev = None
            nextN = head
            while nextN:
        
                temp = ListNode(-1)
                if nextN.next:
                    temp = nextN.next
                nextN.next = prev
                prev = nextN
                if temp.val >=0:
                    nextN = temp
                else:
                    break
            return nextN
        head = reverseL(head)
        carry = 0
        curr = head
        prev = None
        while curr:
            curr.val = curr.val * 2
            curr.val += carry
            carry = 0
            if curr.val > 9:
                curr.val -= 10
                carry = 1
            prev = curr
            curr = curr.next

        
        if carry:
            prev.next = ListNode(carry)
        return reverseL(head)


        