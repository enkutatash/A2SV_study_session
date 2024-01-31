# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        i=0
        while curr:
            i+=1
            curr=curr.next
        f=i-n
        rem=head
        
        if f==0:
            head=head.next
            return head
        j=1
        while rem and j<f:
            rem=rem.next
            j+=1
        
        if rem.next and rem.next.next:
            rem.next=rem.next.next
        else:
            rem.next=None

        return head
        