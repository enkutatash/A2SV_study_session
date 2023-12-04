class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        k=[]
        for i in candies:
            check=i+extraCandies
            if check>=maxi:
                k.append(True)
            else:
                k.append(False)
        return k
        