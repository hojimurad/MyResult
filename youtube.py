word = "LikeLike"
ls = list()
j = 0
dc ={}
for i in range(1,len(word)):
    if word[i].isupper():
        ls.append(word[j:i])
        j = i

# Add the last substring to the list
ls.append(word[j:])



for i in ls:
    if dc.get(i) is None:
      dc[i] = 1
    else:
        dc[i]+=1


print(dc)