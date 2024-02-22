class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        forfinal={v:i for i,v in enumerate(nums1)}
        ans=[-1]*len(nums1)

        stack=[]
        
        for i in nums2:
            while stack and stack[-1]<i:
                z=stack.pop()
                if z in forfinal:
                    ans[forfinal[z]]=i
            
            stack.append(i)
            
            
        return ans 





        