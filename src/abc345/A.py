S = input()
ans = True
for i in range(0, len(S)):
    if (i == 0 and S[i] != '<') or (i != 0 and S[i] == '<'):
        ans = False
        break
    if (i == len(S) - 1 and S[i] != '>') or (i != len(S) - 1 and S[i] == '>'):
        ans = False
        break
print("Yes" if ans else "No")
