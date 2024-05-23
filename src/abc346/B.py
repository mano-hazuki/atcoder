W, B = map(int, input().split())
S = "wbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbw"
ans = False
for i in range(0, len(S)):
    for j in range(0, len(S) - i):
        sub = S[i:i+j+1]
        count_w = 0
        count_b = 0
        for s in sub:
            if s == "w":
                count_w += 1
            if s == "b":
                count_b += 1
            if count_w == W and count_b == B:
                ans = True
                break
print("Yes" if ans else "No")
