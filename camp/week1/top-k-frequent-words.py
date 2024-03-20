class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        bucket = [[] for _ in range(len(words))]
        ans = []
        for i,v in count.items():
            bucket[v].append(i)
        for i in bucket[::-1]:
            if k==0:
                break
            if len(i)==0:
                continue
            else:
                
                i.sort()
                j=0
                while k>0 and j<len(i):
                    ans.append(i[j])
                    k-=1
                    j+=1
        return ans

        
        
        
        