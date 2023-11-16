def fibo(n):
    ls = list()
    ol, hoz = 1, 2

    for _ in range(n):
        ls.append(ol)
        ol, hoz = hoz, ol + hoz

    return ls

ls = fibo(int(input()))
i = 1

while ls:
    row = ls[:i]
    print(""*i,row," ")
    ls = ls[i:]
    i += 1
