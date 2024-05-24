A, B = map(int, input().split())
N = [x for x in range(0, 10)]
N.remove(A + B)
print(N[0])
