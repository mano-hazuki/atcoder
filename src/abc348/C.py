N = int(input())
beans: dict = {}
for _ in range(0, N):
    A, C = map(int, input().split())
    beans[C] = beans[C] if C in beans and beans[C] < A else A
print(max(beans.values()))
