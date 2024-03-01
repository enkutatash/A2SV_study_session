class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0

        def grammer(k,evenness):

            if k==0 and evenness:
                return 0
            elif k==0 and not evenness:
                return 1
            else:
                mid= k//2
                checker=k/2
                if mid==checker:
                    return grammer(k//2,evenness)
                return grammer(k//2,not evenness)
        
        result=grammer(k-1, True)
        return result

        