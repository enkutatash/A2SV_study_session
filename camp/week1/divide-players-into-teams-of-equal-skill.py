class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans=0
        skill.sort()
        start=0
        end=len(skill)-1
        check=skill[start]+skill[end]
        while start<end:
            if skill[start]+skill[end]!=check:
                return -1
            ans+=(skill[start]*skill[end])
            start+=1
            end-=1
        return ans
        