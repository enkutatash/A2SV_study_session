class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        possible_interval=[]
        for i,v in enumerate(intervals):
            possible_interval.append([v[0],i])
        possible_interval.sort(key = lambda a:a[0])
        
        ans = []
        def search(l,r,end):
            nonlocal res
            if l>r:
                return 
            mid = (l+r)//2
            if possible_interval[mid][0]==end:
                res = mid
                return 
            elif possible_interval[mid][0]<end:
                return search(mid+1,r,end)
            else:
                res = mid
                return search(l,mid-1,end)

       
        n=len(possible_interval)
        for ele in intervals:
            start, end = ele
            res = -1
            search(0,n-1,end)
            if res == -1:
                ans.append(-1)
            else:
                ans.append(possible_interval[res][1])
        return ans
