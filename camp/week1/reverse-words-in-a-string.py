class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split())
        k=l[::-1]
        z=" ".join(k)
        return z.strip()
        