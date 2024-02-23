class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dec_queue=deque()
        ans=[]
        n=len(nums)
        for i in range(k):
            while  dec_queue and nums[dec_queue[-1]]<nums[i]:
                dec_queue.pop()
            dec_queue.append(i)
        
        ans.append(nums[dec_queue[0]])
        for i in range(k,n):
            while dec_queue and i-dec_queue[0]>=k:
                dec_queue.popleft()
            while dec_queue and nums[dec_queue[-1]]<nums[i]:
                dec_queue.pop()
            dec_queue.append(i)
            ans.append(nums[dec_queue[0]])
        return ans

        