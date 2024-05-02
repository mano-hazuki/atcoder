S = input()


def is_good(s: str) -> bool:
    good = True
    ascii_offset = ord('a')
    array = list(s)
    counts = [0] * 101  # i回出てきた文字の数が counts[i] に格納される

    for i in range(0, len(counts)):
        count = 0
        for c in array:
            if ord(c) == i + ascii_offset:
                count += 1
        counts[count] += 1

    for i in range(0, len(counts)):
        if i != 0 and counts[i] != 0 and counts[i] != 2:
            good = False
            break
    return good


print("Yes" if is_good(S) else "No")
