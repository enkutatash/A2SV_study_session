class Solution:
    def minFlips(self, target: str) -> int:
        flips=0
        curr='0'
        if target[0]=='1':
            flips+=1
            curr='1'
        

        for i in range(1,len(target)):
            if  target[i]!=curr:
                flips+=1
                curr = '0' if curr=='1' else '1'
        return flips


        