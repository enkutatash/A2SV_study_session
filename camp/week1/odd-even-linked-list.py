# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd1=ListNode()
        odd=odd1
        even1=ListNode()
        even=even1
        curr=head
        i=1
        while curr:
            if i%2==0:
                even.next=curr
                even=even.next
            else:
                odd.next=curr
                odd=odd.next
            curr=curr.next
            i+=1
        even.next=None
        odd.next=even1.next
        return odd1.next

        