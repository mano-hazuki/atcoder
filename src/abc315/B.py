M = int(input())
D = list(map(int, input().split()))
total = sum(D)
mid = total // 2 + 1
i = 0
while True:
    if mid - D[i] <= 0:
        break
    mid = mid - D[i]
    i += 1
print(i + 1, mid)
