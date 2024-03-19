class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        frequency = []
        for i,v in count.items():
            frequency.append([i,v])
        frequency.sort(key = lambda a:a[1],reverse = True)
        i=0
        while i<k:
            result.append(frequency[i][0])
            i+=1
        return result




        