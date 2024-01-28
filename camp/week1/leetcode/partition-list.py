# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr=head
        less=ListNode()
        less1=less
        greater=ListNode()
        greater1=greater
        while curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                greater.next=curr
                greater=greater.next
            curr=curr.next
        greater.next=None
        less.next=greater1.next
        return less1.next
        