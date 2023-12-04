class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1="".join(word1)
        l2="".join(word2)
        if l1==l2:
            return True
        else:
            return False
        