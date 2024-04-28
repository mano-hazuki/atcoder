N = int(input())
A = list(map(int, input().split()))
array = []
for i in range(0, N):
    array.append(A[i])
    # print("Appended", array)

    if len(array) == 1:
        continue
    while array[-1] == array[-2]:
        new = array[-1] + 1

        del array[-1]
        # print("Deleted last item",  array)
        del array[-1]
        # print("Deleted last item",  array)
        array.append(new)
        # print("Appended new item",  array)

        if len(array) == 1:
            break
print(len(array))
