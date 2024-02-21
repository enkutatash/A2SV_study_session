class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers=[i+1 for i in answers]
        ans=Counter(answers)
        result=0
        for i,v in ans.items():
            if i==0:
                result+=v
            else:
                q=v//i
                result+=(q*i)
                r=v%i
                if r!=0:
                    result+=(i)
        return result




        