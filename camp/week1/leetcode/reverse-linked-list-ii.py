# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        pend = prev.next
        leftend = pend.next
        for i in range(right - left):
            pend.next = leftend.next
            leftend.next = prev.next
            prev.next =leftend
            leftend = pend.next
        return dummy.next