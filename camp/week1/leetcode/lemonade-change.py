class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=defaultdict(int)

        for i in bills:
            if i==5:
                change[5]+=1
            elif i==10:
                if change[5]==0:
                    return False
                else:
                    change[5]-=1
                    change[10]+=1
            else:
                if change[10]>0 and change[5]>0:
                    change[10]-=1
                    change[5]-=1
                    change[20]+=1
                elif change[5]>=3:
                    change[5]-=3
                    change[20]+=1
                else:
                    return False
        return True

        