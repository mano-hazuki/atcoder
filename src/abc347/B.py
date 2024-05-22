S = input()
combs = set()

for i in range(0, len(S)):
    for j in range(i, len(S)):
        combs.add(S[i:j+1])
print(len(combs))
