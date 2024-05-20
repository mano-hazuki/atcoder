N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(0, N - 1):
    for j in range(i + 1, N):
        s = A[i] + A[j]
        if s < 100000000:
            ans += s
        elif s > 100000000:
            ans += s % 100000000
print(ans)
