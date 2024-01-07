class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        longestT=0
        longestF=0
        leftT=0
        leftF=0
        z=k
        for ele in range(len(answerKey)):
            if answerKey[ele]=="F":
                k-=1
            while k<0:
                if answerKey[leftT]=="F":
                    k+=1
                leftT+=1
            longestT=max(longestT,ele-leftT+1)
        for ele in range(len(answerKey)):
            if answerKey[ele]=="T":
                z-=1
            while z<0:
                if answerKey[leftF]=="T":
                    z+=1
                leftF+=1
            longestF=max(longestF,ele-leftF+1)
        return max(longestT,longestF)
        