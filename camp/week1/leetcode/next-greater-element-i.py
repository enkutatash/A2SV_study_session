class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        forfinal={v:i for i,v in enumerate(nums2)}
        ans=[-1]*len(nums1)

        for i in range(len(nums1)):
            innums2=forfinal[nums1[i]]
            for j in range(innums2+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
        return ans

        