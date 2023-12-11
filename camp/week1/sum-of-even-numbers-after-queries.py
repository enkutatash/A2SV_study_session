class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even={}
        even_sum=[]
        for i,v in enumerate(nums):
            if v %2 ==0:
                even[i]=v
            else:
                even[i]=0

        for i in queries:
            nums[i[1]]+=i[0]
            if nums[i[1]]%2==0:
                even[i[1]]=nums[i[1]]
            else:
                even[i[1]]=0

            even_sum.append(sum(even.values()))
        return even_sum



        