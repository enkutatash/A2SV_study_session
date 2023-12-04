class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(0,len(nums),2):
            k+=[nums[i+1]]*nums[i]
        return k
        