class Solution:
    def average(self, salary: List[int]) -> float:
        mini=min(salary)
        maxi=max(salary)
        total=sum(salary)
        length=len(salary)-2
        average=(total-(mini+maxi))/length
        return average

        