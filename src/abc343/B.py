N = int(input())
A = [list(map(int, input().split())) for i in range(0, N)]
V = [set() for _ in range(0, N)]

for y in range(0, N):
    for x in range(0, N):
        if A[y][x] == 1:
            V[y].add(x)
            V[x].add(y)
for v in V:
    arr = sorted(list(v))
    for i in arr:
        print(i + 1, "", end="")
    print()
