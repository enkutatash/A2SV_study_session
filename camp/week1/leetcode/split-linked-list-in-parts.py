# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        n=0
        while curr:
            n+=1
            curr=curr.next
        ans=[]
        curr=head
        rem=n%k
        que=n//k
        while k:
            ans.append(curr)
            k-=1
            prev=ListNode()
            for i in range(que):
                prev=curr
                curr=curr.next
            if rem!=0:
                prev=curr
                curr=curr.next
                rem-=1
            prev.next=None
        return ans
            



        