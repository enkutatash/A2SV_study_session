def checker(test,check):
    for i,v in check.items():
        if check[i]>test[i]:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window=""
        check=Counter(t)
        test={i:0 for i in t}
        left=0
        for right in range(len(s)):
            if s[right] in test:
                test[s[right]]+=1
            while checker(test,check):
                if len(window)==0:
                    window=s[left:right+1]
                elif len(window)>right-left+1:
                    window=s[left:right+1]
                if s[left] in test:
                    test[s[left]]-=1
                left+=1
        return window
                
            



        