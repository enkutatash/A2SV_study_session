class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans=1
        points.sort(key=lambda a:(a[0],a[1]))
        start=points[0][0]
        end=points[0][1]
       
        for i in points[1:]:
            if i[0]>end:
                ans+=1
                start=i[0]
                end=i[1]
            elif i[0]>start:
                start=i[0]
                if i[1]<end:
                    end=i[1]
            else:
                continue
        return ans

        