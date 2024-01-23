class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*(len(nums)+1)
        for i in requests:
            prefix[i[0]]+=1
            prefix[i[1]+1]-=1

        build=list()
        total=0
        for i in prefix[:-1]:
            total+=i
            build.append(total)

        buildL=list()
        for i,v in enumerate(build):
            buildL.append([v,i])
        buildL=sorted(buildL,reverse=True,key=lambda a:a[0])
        
        permutation=[0]*len(nums)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            z=buildL[i][1]
            permutation[z]=nums[i]
        
        pre=[]
        t=0
        for i in permutation:
            t+=i
            pre.append(t)
        
        sumup=0
        for i,j in requests:
            sumup+=pre[j]
            if i!=0:
                sumup-=pre[i-1]
        return sumup%(pow(10,9)+7)

        
        