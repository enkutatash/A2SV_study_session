class Solution:
    def maxScore(self, s: str) -> int:
        one=s.count('1')
        zero=0
        result=0
        for i in s[:-1]:
            if i=='1':
                one-=1
            if i=='0':
                zero+=1
            result=max(result,zero+one)
        return result
        