class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            sample=Counter(s2[i:i+len(s1)])
            if check==sample:
                return True
        return False
        
        