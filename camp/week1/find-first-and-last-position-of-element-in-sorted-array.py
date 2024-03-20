class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        def binary(l,r):
            if l>r:
                return
            mid = (l+r)//2
            if nums[mid]==target:
                if ans[0]==-1:
                    ans[0]=mid
                elif ans[0]>mid:
                    ans[0]=mid
                if ans[1]==-1:
                    ans[1]=mid
                elif ans[1]<mid:
                    ans[1]=mid
            binary(l,mid-1)
            binary(mid+1,r)
        binary(0,len(nums)-1)
        return ans


        