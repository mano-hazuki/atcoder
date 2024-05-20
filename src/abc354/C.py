N = int(input())
L = []
max_A = 0
target_C = 0
for i in range(0, N):
    A, C = map(int, input().split())
    max_A = A if A > max_A else max_A
    target_C = C if A == max_A else target_C
    L.append(C)
L.sort()
left = -1
right = N
while right - left > 1:
    mid = left + (right - left) // 2
    if L[mid] >= target_C:
        left = mid
    else:
        right = mid


