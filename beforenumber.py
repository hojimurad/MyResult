

# i= 0
# dc ={}
#
# while i<7:
#     a = int(input())
#     if dc.get(a) is None:
#         print("Yes")
#         dc[a]=1
#
#     else:
#         print("NO")
#     i+=1

dc = {}
ls  = list(map(int,input().split()))

for i in ls:
    if dc.get(i) is None:
        print("NO")
        dc[i]=1

    else:
        print("YES")
