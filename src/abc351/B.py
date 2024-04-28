N = int(input())
A = [list(map(str, input())) for _ in range(0, N)]
B = [list(map(str, input())) for _ in range(0, N)]

for i in range(0, N):
    for j in range(0, N):
        if A[i][j] != B[i][j]:
            print(f'{i + 1} {j + 1}')
            break
