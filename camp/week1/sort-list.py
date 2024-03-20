# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        def middle(head):
            if not head:
                return head
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def mergesort(left):
            if not left or not left.next :
                return left
            mid = middle(left)
            
            next_mid = mid.next
            mid.next = None 
            l = mergesort(left)
            r = mergesort(next_mid)
            sortedl = merge(l,r)
            return sortedl
        def merge(left,right):
            
            dummy = ListNode()
            head = dummy
        
            while left and right:
                if left.val<right.val:
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next
                dummy = dummy.next
            if left :
                dummy.next = left
            if right:
                dummy.next = right
            return head.next
        
        ans = mergesort(head)
        
        return ans

        