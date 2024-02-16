from collections import defaultdict
test=int(input())
for _ in range(test):
    length=int(input())
    li=[int(i) for i in input()]
    check=defaultdict(int)
    check[0]=1

    ans=sumup=0

    for i in range(length):
        sumup+=li[i]
        remove=sumup-i-1
        check[remove]+=1
        ans+=check[remove]-1
    print(ans)
    

    