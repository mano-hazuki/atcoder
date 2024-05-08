S = input()
T = input()
ans: list[int] = []
i = 0
for s in S:
    if len(ans) > 0 and ans[-1] == i:
        i += 1
    while s != T[i]:
        i += 1
    ans.append(i)

for a in ans:
    print(f"{a + 1} ")
