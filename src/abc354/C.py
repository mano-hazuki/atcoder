import math

N = int(input())
A_C_I = []
for i in range(0, N):
    A_C_I.append(list(map(int, input().split())))
    A_C_I[i].append(i)
A_C_I.sort()
A_C_I.reverse()

max_cost = math.inf
ans = []

for A, C, i in A_C_I:
    if C <= max_cost:
        ans.append(i + 1)
        max_cost = C

ans.sort()

print(len(ans))
for a in ans:
    print(a, "", end="")
