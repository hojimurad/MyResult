
n = int(input())
ls = list(map(int,input().split()))

a = ls.copy()
for i in set(ls):
    if a.count(i)>=3:
        print(i,end=" ")
    else:
        continue