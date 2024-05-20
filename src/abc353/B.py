N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
cur = 0
for a in A:
    if K - cur >= a:
        cur += a
        continue
    ans += 1
    cur = a
print(ans + 1)
