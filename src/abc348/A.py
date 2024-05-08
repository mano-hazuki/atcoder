N = int(input())
for i in range(0, N):
    if (i + 1) % 3 == 0:
        print('x', end="")
    else:
        print('o', end="")
print()
