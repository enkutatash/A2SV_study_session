class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sumup=0
        prefix=[]
        for i in arr:
            sumup+=i
            prefix.append(sumup)

        ans=0
        for right in range(len(arr)):
            left=right
            while left<len(arr):
                if left==right:
                    ans+=arr[right]
                elif (right-left+1)%2!=0:
                    ans+=prefix[left]
                    if right-1>=0:
                        ans-=prefix[right-1]
                left+=1
        return ans

        