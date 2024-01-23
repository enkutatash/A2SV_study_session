# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        h1=prev
        h2=head
        while h2 and h1:
            if h1.val!=h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True


        