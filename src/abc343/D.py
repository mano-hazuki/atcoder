N, T = map(int, input().split())
C = [0 for _ in range(0, N)]

for _ in range(0, T):
    A, B = map(int, input().split())
    C[A - 1] += B
    D = set(C)
    print(len(D))
