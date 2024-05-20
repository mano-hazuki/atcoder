def check(s: str) -> bool:
    for index in range(0, len(s) // 2):
        start = index
        end = len(s) - 1 - index
        if s[start] != s[end]:
            return False
    return True


S = input()
ans = 0
for i in range(0, len(S)):
    for j in range(0, len(S) + 1):
        text = S[i:len(S) - j]
        if check(text):
            ans = len(text) if len(text) > ans else ans;
print(ans)
