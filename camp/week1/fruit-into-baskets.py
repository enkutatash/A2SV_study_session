class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window=defaultdict(int)
        left=0
        maxfruit=0
        for right in range(len(fruits)):
            window[fruits[right]]+=1
            while len(window)>2:
                window[fruits[left]]-=1
                if window[fruits[left]]==0:
                    del window[fruits[left]]
                left+=1
            maxfruit=max(maxfruit,right-left+1)
        return maxfruit