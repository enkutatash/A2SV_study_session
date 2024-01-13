class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        most_fre=0
        length=0
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            most_fre=max(most_fre,freq[s[right]])
            if right-left+1-most_fre>k:
                freq[s[left]]-=1
                left+=1
            length=max(length,right-left+1)
        return length

        