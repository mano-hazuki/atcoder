N, K = map(int, input().split())
A = list(map(int, input().split()))
ans: list[int] = []

for a in A:
    if a % K == 0:
        ans.append(a // K)
ans = sorted(ans)
for a in ans:
    print(a, " ", end="")
print()
