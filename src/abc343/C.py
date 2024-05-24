# X_MAX = 1000000
# L = []
# for i in range(0, X_MAX + 1):
#     L.append(pow(i, 3))
# for l in L:
#     S = str(l)
#     satisfies = True
#     for i in range(0, len(S) // 2):
#         if S[i] != S[len(S) - 1 - i]:
#             satisfies = False
#             break
#     if satisfies:
#         print(l)

nums = [0, 1, 8, 343, 1331, 1030301, 1367631, 1003003001, 10662526601, 1000300030001, 1030607060301, 1334996994331, 1000030000300001, 1033394994933301, 1331399339931331]
nums.reverse()
N = int(input())

for n in nums:
    if n <= N:
        print(n)
        break
