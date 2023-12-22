class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        result=defaultdict(list)
        zero=0
        one=sum(nums)
        for i in range(len(nums)):
            result[zero+one].append(i)
            if nums[i]==0:
                zero+=1
            else:
                one-=1
        result[zero+one].append(len(nums))
        z=max(result)
        return result[z]
    