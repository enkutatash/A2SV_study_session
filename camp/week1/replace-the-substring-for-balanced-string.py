def check(temp,extra):
    for i in extra.keys():
        if extra[i]>temp[i]:
            return False
    return True

class Solution:
    def balancedString(self, s: str) -> int:
        hash=Counter(s)
        extra=defaultdict(int)
        n=len(s)
        for i,v in hash.items():
            if v>n/4:
                extra[i]=v-n/4
        
        left=0
        small=float('inf')
        temp=defaultdict(int)
        if len(extra)==0:
            return 0
        print(extra)
        for right in range(n):
            if s[right] in extra:
                temp[s[right]]+=1
            while check(temp,extra):
                    small=min(small,right-left+1)
                    if s[left] in extra:
                        temp[s[left]]-=1
                    left+=1
        return small if small!=float('inf') else 0

        