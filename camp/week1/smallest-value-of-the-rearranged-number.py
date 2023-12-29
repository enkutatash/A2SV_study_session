class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        else:
            n=list()
            num1=abs(num)
            while num1!=0:
                n.append(num1%10)
                num1//=10
                 
            zero=n.count(0)
        
            if num>0:
                n.sort()
                if zero!=0:
                    n=n[zero:]
                    n=[n[0]]+[0]*zero+n[1:]
                
            else:
                n.sort(reverse=True)
                if zero!=0:
                    n=n[:-zero]
                    n.extend([0]*zero)
            final=0
            for i in n:
                final*=10
                final+=i
                
            if num<0:
                return -final
            return final
                


        