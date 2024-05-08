import math
N = int(input())
points: list[list[int]] = []
for i in range(0, N):
    points.append(list(map(int, input().split())))
for i in range(0, N):
    max_dist = -1
    max_dist_i = -1
    current = points[i]
    for j in range(0, N):
        point = points[j]
        if current[0] == point[0] and current[1] == point[1]:
            continue
        dist = math.sqrt(abs(current[0] - point[0]) ** 2 + abs(current[1] - point[1]) ** 2)
        if dist > max_dist:
            max_dist = dist
            max_dist_i = j
    print(max_dist_i + 1)
