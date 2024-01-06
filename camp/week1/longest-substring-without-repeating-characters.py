class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        exist={}
        longest=0
        while right<len(s):
            while s[right] in exist:
                exist[s[left]]-=1
                if exist[s[left]]==0:
                    del exist[s[left]]
                left+=1
            exist[s[right]]=1
            longest=max(longest,len(exist))
            right+=1
        return longest
                


        