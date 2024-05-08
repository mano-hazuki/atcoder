def get_nearest(raw: list[str]) -> list[str]:
    found_first: bool = False
    for i in range(0, len(raw)):
        if raw[i] == '1':
            if found_first:
                raw[i] = '0'
            else:
                found_first = True
                continue
    return raw


L, R = map(bin, map(int, input().split()))
L = list(L)
R = list(R)

temp = get_nearest(R)