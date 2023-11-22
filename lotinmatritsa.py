n = int(input())

# Initialize ls as a list of lists with dimensions n x n
ls = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        ls[i][j] = int(input())


def check(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ls[i][j] not in list(range(n)):
                print("No")
                return
    print("yes")

# Call the show function
check(ls)
