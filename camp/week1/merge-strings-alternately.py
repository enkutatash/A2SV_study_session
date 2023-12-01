class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mini=min(len(word1),len(word2))
        result=''
        for i in range(mini):
            result+=word1[i]
            result+=word2[i]
        result+=word1[mini:]
        result+=word2[mini:]
        return result
        