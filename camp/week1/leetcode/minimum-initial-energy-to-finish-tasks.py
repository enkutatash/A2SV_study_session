class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(reverse=True,key=lambda a:a[1]-a[0])
        now=tasks[0][1]-tasks[0][0]
        ans=tasks[0][1]
        for i in tasks[1:]:
            ac,mi=i
            v=0
            if mi>now:
                v=(mi-now)
            now+=v
            now-=ac
            ans+=v
        return ans

