# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ele=set()
        prev=head
        curr=head
        while head:
            if head.val not in ele:
                ele.add(head.val)
                prev=head
            else:
                prev.next=head.next
            head=head.next
        return curr
