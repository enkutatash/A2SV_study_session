from bisect import bisect_right
n=int(input())
shop = list(map(int,input().split()))
shop.sort()
q=int(input())
for _ in range(q):
  coin=int(input())
  print(bisect_right(shop,coin))