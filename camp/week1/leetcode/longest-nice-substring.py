class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        def nice(l,r):
            nonlocal ans
            if l>=r :
                return 
            temp = set(s[l:r])
            curr=l
            for i in range(l,r):
                if s[i].swapcase() not in temp:
                    curr= i
                    break
            else:
                if len(ans)<r-l+1:
                    ans = s[l:r]
                return
            nice(curr+1,r)
            nice(l,curr)
           
            return 
        nice(0,len(s))
        return ans




