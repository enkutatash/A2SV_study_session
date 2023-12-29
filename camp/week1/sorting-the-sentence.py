class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        word=sorted(s,key=lambda a:a[-1])
        k=""
        k=" ".join(i[:-1] for i in word)
        
            
        return k
        