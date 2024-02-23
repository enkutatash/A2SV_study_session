class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[]
        count=0
        for i in nums:
            if len(stack)==0:
                stack.append(i)
            else:
                if i!=stack[-1]:
                    stack.pop()
                else:
                    count+=1
        if stack:
            count+=1
        return count
        