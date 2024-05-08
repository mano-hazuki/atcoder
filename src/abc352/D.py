N, K = map(int, input().split())
P_input = [num for num in list(map(int, input().split()))]
P_index = [num for num in range(0, N)]
P: list[list[int]] = [[P_input[i], P_index[i]] for i in range(0, N)]
ans = 0


