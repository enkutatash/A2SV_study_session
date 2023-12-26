class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights)):
            maxi=i
            for j in range(i+1,len(heights)):
                if heights[j]>heights[maxi]:
                    maxi=j
            heights[maxi],heights[i]=heights[i],heights[maxi]
            names[maxi],names[i]=names[i],names[maxi]
        return names
        