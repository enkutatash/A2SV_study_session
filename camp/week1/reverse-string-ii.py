class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li=[]
        for i in range(len(s)):
            if (i//k)%2==0:
               li.insert(i-i%k,s[i])
            else:
                li.append(s[i])
        res=""
        for t in li:
            res+=t
        return res