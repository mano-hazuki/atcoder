N, K = map(int, input().split())
A = set(map(int, input().split()))

total = (1 + K) * K // 2
for a in A:
    if a > K:
        continue
    total -= a
print(total)
