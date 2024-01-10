class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        sub=""
        longest=0
        sample=defaultdict(int)
        for right in range(len(s)):
            sample[s[right]]+=1
            while sample[s[right]]>1:
                sample[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest
             


        