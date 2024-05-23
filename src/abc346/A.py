N = int(input())
A = list(map(int, input().split()))

for i in range(0, len(A) - 1):
    print(A[i] * A[i + 1], "", end="")
