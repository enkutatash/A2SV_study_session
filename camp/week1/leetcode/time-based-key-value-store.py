class TimeMap:

    def __init__(self):
        self.time_map=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        allTime=self.time_map[key]
       
        left=0
        right = len(allTime)-1
        ans = -1
        def search(left,right):
            nonlocal ans
            if left>right:
                return -1
            mid = (left+right)//2
            if allTime[mid][0]==timestamp:
                ans = mid
                return
            elif allTime[mid][0]>timestamp:
                return search(left,mid-1)
            else:
                ans = mid
                return search(mid+1,right)
        search(left,right)
        if ans==-1:
            return ""
        else:
            return allTime[ans][1]

        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)