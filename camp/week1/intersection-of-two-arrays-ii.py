class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1=Counter(nums1)
        num2=Counter(nums2)
        nums1=set(nums1)
        nums2=set(nums2)
        num3=nums1 and nums2
        li=[]
        for i in num3:
            l=min(num1[i], num2[i])
            li.extend([i]*l)
        return li

        