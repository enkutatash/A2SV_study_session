# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            check = curr.next

            
            while check:
                if check.val < curr.val:
                    temp = curr.val
                    curr.val = check.val
                    check.val = temp
                check = check.next
            curr = curr.next
        return head