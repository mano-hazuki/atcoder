N = int(input())
A = sorted(list(map(int, input().split())))
for i in range(0, N - 1):
    if A[i + 1] - A[i] > 1:
        print(A[i] + 1)
        break
