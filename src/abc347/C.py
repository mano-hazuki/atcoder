N, A, B = map(int, input().split())
D = list(map(int, input().split()))
ans = False

for i in range(0, A + B):
    for d in D:
        if d + i % (A + B) <= A:
            ans = True
            break
print("Yes" if ans else "No")
