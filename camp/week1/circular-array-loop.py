class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        for right in range(len(nums)):
            visit=set()
            current=right
            while True:
                z=(current+nums[current])%n
                if z in visit:
                    return True
                if z==current:
                    break
                else:
                    if nums[current]*nums[z]<0:
                        break
                    visit.add(current)
                    current=z
        return False