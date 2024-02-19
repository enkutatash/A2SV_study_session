class Solution:
    def longestPalindrome(self, s: str) -> int:
        maped=Counter(s)
        single=False
        longest=0
        for i,v in maped.items():
            if v%2==0:
                longest+=v
            else:
                single=True
                longest+=(v-1)
        if single:
            longest+=1
        return longest

        