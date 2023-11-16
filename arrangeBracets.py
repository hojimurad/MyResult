
word =input()

natija = ""
if len(word) % 2==1:
    mid = len(word) // 2
    mid_index = word.index(word[mid])
    for i in range(0, mid_index+1):
        natija = natija + "(" + word[i]
    for i in range(mid_index+1, len(word)):
        natija = natija + ")" +word[i]
    natija = natija + ")"



else:
    mid = len(word)//2
    mid_index = word.index(word[mid])
    for i in range(0,mid_index):
        natija = natija+"("+word[i]
    for i in range(mid_index,len(word)):
        natija = natija+word[i]+")"
print(natija)
