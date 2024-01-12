class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        allsum=sum(cardPoints)
        z=len(cardPoints)-k
        window=sum(cardPoints[:z])
        minisum=window
        left=0
        for right in range(z,len(cardPoints)):
            window+=cardPoints[right]
            window-=cardPoints[left]
            minisum=min(minisum,window)
            left+=1
        return sum(cardPoints)-minisum

        
        