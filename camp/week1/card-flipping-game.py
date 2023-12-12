class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good=float("inf")
        same=set()
        for i, v in zip(fronts,backs):
            if i==v:
                same.add(i)
        for i in fronts:
            if i not in same:
                good=min(good,i)
        for j in backs:
            if j not in same:
                good=min(good,j)
            
        return good if good!=float("inf") else 0


        