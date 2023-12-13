class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique={}
        for i in s:
            unique[i]=1
        return len(unique)
        