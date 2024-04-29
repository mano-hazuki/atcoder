N, Q = map(int, input().split())
T = list(map(int, input().split()))
arr = [1] * N

for i in range(0, Q):
    index = T[i] - 1
    if arr[index] == 1:
        arr[index] = 0
    else:
        arr[index] = 1

ans = 0
for j in range(0, N):
    if arr[j] == 1:
        ans += 1

print(ans)
