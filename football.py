

uzbek =0
other = 0

li =[0,0]

ls =input().split()



for i in ls:
    if int(i[0])>int(i[2]):
        uzbek+=3
        li[0]+=int(i[0])
        li[1]+= int(i[2])
    elif int(i[0])<int(i[2]):
        li[0] += int(i[0])
        li[1] += int(i[2])
        uzbek+=0
    else:
        li[0] += int(i[0])
        li[1] += int(i[2])
        uzbek+=1
print(f"{uzbek}  {li[0]}-{li[1]}")