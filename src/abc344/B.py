from collections import deque

q = deque([])

while True:
    A = int(input())
    q.append(A)
    if A == 0:
        break
for _ in range(0, len(q)):
    print(q.pop())
