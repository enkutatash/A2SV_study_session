class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        left=0
        right=len(s)-1
        n=len(s)
        while left<right:
            while left<n and s[left]!='1':
                left+=1
            while right>=0 and s[right]!='0':
                right-=1
            if left<right:
                count+=(right-left)
                left+=1
                right-=1
        return count
