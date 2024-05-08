N = int(input())
P: list[list[int]] = []
diff_max = 0
i_top = 0
ans = 0
for i in range(0, N):
    A, B = map(int, input().split())
    P.append([A, B])

    diff = B - A
    if diff > diff_max:
        diff_max = abs(diff)
        i_top = i
for i in range(0, N):
    if i == i_top:
        ans += P[i][1]
    else:
        ans += P[i][0]
print(ans)
