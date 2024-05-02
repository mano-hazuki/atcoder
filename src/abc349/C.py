S = list(input())
S += ["x"]
T = list(input().lower())
index: int = 0
for s in S:
    if index == 3:
        break
    if s == T[index]:
        index += 1

print("Yes" if index == 3 else "No")
