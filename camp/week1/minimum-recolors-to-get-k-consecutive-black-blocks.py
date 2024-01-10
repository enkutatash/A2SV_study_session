class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sample=blocks[:k]
        sampleCount=sample.count("W")
        minope=sampleCount
        i=0
        r=0
        while i<len(blocks)-k:
            if blocks[i+k]=="W":
                sampleCount+=1
            if blocks[r]=="W":
                sampleCount-=1
            minope=min(minope,sampleCount)
            r+=1
            i+=1
        return minope
