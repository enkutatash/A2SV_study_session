# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged=ListNode()
        head=merged

        def merge(list1,list2,merged):
            if list2==None:
                merged.next=list1
            elif list1==None:
                merged.next=list2
            elif list1.val<=list2.val:
                merged.next=ListNode(list1.val)
                list1=list1.next
                merged=merged.next
                merge(list1,list2,merged)
            else:
               
                merged.next=ListNode(list2.val)
                list2=list2.next
                merged=merged.next
                merge(list1,list2,merged)
        merge(list1,list2,merged)
        return head.next          

        