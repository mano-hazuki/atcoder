N = int(input())
H = list(map(int, input().split()))
ans = -2
for i in range(0, N):
    if i == 0:
        continue
    if H[i] > H[0]:
        ans = i
        break
print(ans + 1)
