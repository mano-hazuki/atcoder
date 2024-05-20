N = int(input())
names = []
score_total = 0
for i in range(0, N):
    S, C = map(str, input().split())
    names.append(S)
    score_total += int(C)
index = score_total % N
names = sorted(names)
print(names[index])
