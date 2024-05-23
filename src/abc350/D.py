N, M = map(int, input().split())
friends = [[] for _ in range(0, N)]
for _ in range(0, M):
    A, B = map(int, input().split())
    friends[A - 1].append(B - 1)
    friends[B - 1].append(A - 1)
# for i in range(0, N):
#     for j in range(0, len(friends[i]) - 1):
#         for k in range(j + 1, len(friends[i])):
#             if friends
