class Solution:
    def romanToInt(self, s: str) -> int:
        klist={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result=0
        for i in range(len(s)):
            c=s[i]
            d=s[i]
            if i<len(s)-1:
                d=s[i+1]
            if klist[c]>=klist[d]:
                result+=klist[c]
            else:
                result-=klist[c]
        return result
        