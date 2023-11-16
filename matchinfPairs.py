ls = list(map(int, input().split()))
cnt = 0
dc = {}

# Count occurrences of each element in the list
for i in ls:
    if dc.get(i) is None:
        dc[i] = 1
    else:
        dc[i] += 1

# Calculate the count of matching pairs
for i in set(ls):
    if dc[i] == 2:
        cnt += 1  # Increment by 1 for each pair
    elif dc[i] > 2:
        cnt += (dc[i] * (dc[i] - 1)) // 2  # Use dc[i] instead of cnt

print(cnt)
