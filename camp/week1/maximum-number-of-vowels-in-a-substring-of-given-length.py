class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        longest=0
        left=0
        count=0
        max_count=0
        for ele in range(len(s)):
            if s[ele] in "aeiou":
                count+=1
            while ele-left+1>k:
                if s[left] in "aeiou":
                    count-=1
                left+=1
            max_count=max(max_count,count)
        return max_count
            

        