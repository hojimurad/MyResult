ls = input().split()

natija = ""

if len(ls) == 0:
    natija = "no one like this"
elif len(ls) == 1:
    natija = f"{ls[0]} like this"
elif len(ls) == 2:
    natija = f"{ls[0]} and {ls[1]} like this"
else:
    for i in range(len(ls) - 1):
        if i == len(ls) - 2:
            natija = natija + f"{ls[i]} and {ls[i + 1]} like this"
        else:
            natija = natija + ls[i] + ", "

print(natija)
