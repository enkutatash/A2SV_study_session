class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        mini=min(start,destination)
        maxi=max(start,destination)
        left=sum(distance[mini:maxi])
        right=sum(distance[:mini])+sum(distance[maxi:])
        return min(left,right)

        