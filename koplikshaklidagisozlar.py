

words = input().split()



dc = {}

for i in words:
    if dc.get(i) is None:
        dc[i] =1
    else:
        dc[i]+=1

new_dc={}
for k,v in dc.items():
    if v>=2:
        new_dc[k+"s"]=v
    else:
        new_dc[k] =v
print(set(new_dc.keys()))

