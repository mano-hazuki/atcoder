H = int(input())
now = 0
ans = 0

while now <= H:
    now += pow(2, ans)
    ans += 1

print(ans)
