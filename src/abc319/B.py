N = int(input())
for i in range(0, N + 1):
    exists = False
    for j in range(1, 10):
        if N % j == 0 and i % (N // j) == 0:
            print(j, end="")
            exists = True
            break
    if not exists:
        print("-", end="")
