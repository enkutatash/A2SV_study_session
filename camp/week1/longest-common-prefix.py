class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        strs=sorted(strs)
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if(strs[0][i]!=strs[-1][i]):
                return pre
            else:
                pre+=strs[0][i]
        return pre