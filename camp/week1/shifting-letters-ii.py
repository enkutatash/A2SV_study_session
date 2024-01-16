class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        li=list(ord(i) for i in s)
        news=[0]*(len(li))
        for i in shifts:
            if i[2]==1:    
                news[i[0]]+=1
                if i[1]<len(li)-1:
                    news[i[1]+1]-=1
            else:
                news[i[0]]-=1
                if i[1]<len(li)-1:
                    news[i[1]+1]+=1
        new=list()
        sumi=0
        for i in news:
            sumi+=i
            new.append(sumi)
        print(news)
        print(new)
        print(li)
        for i in range(len(li)):
            li[i]+=new[i]%26
            if li[i]>122:
                li[i]%=122
                li[i]+=96
            elif li[i]<97:
                li[i]+=26
        a="".join(chr(i) for i in li)
        return a

        