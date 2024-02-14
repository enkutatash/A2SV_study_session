class Solution:
    def numberOfWays(self, s: str) -> int:
        zero=one=answer=0
        totalzero=s.count('0')
        totalone=s.count('1')
        #mid zero
        for i in s:
            if i=='0':
                answer+=(one*(totalone-one))
            else:
                one+=1
        #mid one
        for i in s:
            if i=='1':
                answer+=(zero*(totalzero-zero))
            else:
                zero+=1
        return answer








        